import asyncio
import copy
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional

from aiconfig.schema import AIConfig, ExecuteResult, Output, Prompt

if TYPE_CHECKING:
    from aiconfig.Config import AIConfigRuntime


class ModelParser(ABC):
    @abstractmethod
    def id(self) -> str:
        """
        Returns an identifier for the model (e.g. llama-2, gpt-4, etc.).
        """

    @abstractmethod
    async def serialize(
        self,
        prompt_name: str,
        data: Any,
        ai_config: "AIConfigRuntime",
        parameters: Optional[Dict] = None,
        **kwargs,
    ) -> List[Prompt]:
        """
        Serialize a prompt and additional metadata/model settings into a
        list of Prompt objects that can be saved in the AIConfig.

        Args:
            prompt_name (str): Name to identify the prompt.
            data (Any): The prompt data to be serialized.
            ai_config (AIConfig): The AIConfig that the prompt belongs to.
            parameters (dict, optional): Optional parameters to include in the serialization.
            **kwargs: Additional keyword arguments, if needed.

        Returns:
            List[Prompt]: Serialized representation of the input data.
        """

    @abstractmethod
    async def deserialize(
        self,
        prompt: Prompt,
        aiConfig: "AIConfigRuntime",
        params: Optional[Dict] = None,
    ) -> Any:
        """
        Deserialize a Prompt object loaded from an AIConfig into a structure that can be used for model inference.

        Args:
            prompt (Prompt): The Prompt object from an AIConfig to deserialize into a structure that can be used for model inference.
            aiConfig (AIConfigRuntime): The AIConfig that the prompt belongs to.
            params (dict, optional): Optional parameters to override the prompt's parameters with.

        Returns:
            R: Completion params that can be used for model inference.
        """

    @abstractmethod
    async def run(
        self,
        prompt: Prompt,
        aiconfig: AIConfig,
        options: Optional["InferenceOptions"] = None,
        parameters: Dict = {},
        **kwargs,  # TODO: Remove this, just a hack for now to ensure that it doesn't break
    ) -> ExecuteResult:
        """
        Execute model inference based on completion data to be constructed in deserialize(), which includes the input prompt and
        model-specific inference settings. Saves the response or output in prompt.outputs.

        Args:
            prompt (Prompt): The prompt to be used for inference.
            aiconfig (AIConfig): The AIConfig object containing all prompts and parameters.
            options (InferenceOptions, optional): Options that determine how to run inference for the prompt
            parameters (dict, optional): Optional parameters to include in the serialization.

        Returns:
            ExecuteResult: The response generated by the model.
        """

    async def run_batch(
        self,
        prompt: Prompt,
        aiconfig: "AIConfigRuntime",
        parameters_list: list[dict[str, Any]],
        options: Optional["InferenceOptions"] = None,
        **kwargs: Any,
    ) -> list["AIConfigRuntime"]:
        """
        Concurrently runs inference on multiple parameter sets, one set at a time.
        Default implementation for the run_batch method. Model Parsers may choose to override this method if they need to implement custom batch execution logic.
        For each dictionary of parameters in `params_list``, the `run` method is invoked. All iterations are separate as we use a deep copy of `aiconfig` in each iteration.

        Args:
            prompt (Prompt): The prompt for running the inference
            aiconfig (AIConfigRuntime): The AIConfig object containing all necessary configurations (prompts and parameters) for running the inference.
            parameters_list (list[dict[str, Any]]): A List of dictionaries, where each dictionary is a set of parameters that directly influence the behaviour of inference.
            options (InferenceOptions, optional): Options to tune the execution of inference, like setting timeout limits, number of retries, etc.
            **kwargs: Additional arguments like metadata or custom configuration that could be used to modify the inference behaviour.

        Returns:
            list[AIConfigRuntime]: A list of AIConfigRuntime objects. Each object contains the state of the AIConfigRuntime after each run using the corresponding parameter set from params_list.
        """
        # Intiailize an empty list to hold the results
        inference_results = []
        tasks = []

        for params in parameters_list:
            # Create a deep copy of the aiconfig object to prevent mutations that could affect other iterations
            aiconfig_deep_copy = copy.deepcopy(aiconfig)
            prompt = aiconfig_deep_copy.get_prompt(prompt.name)
            # Asynchronously schedule 'run()' for execution with a set of parameters.
            # This approach enables concurrent processing of multiple aiconfigs.
            task = asyncio.create_task(
                self.run(prompt, aiconfig_deep_copy, options, params, **kwargs)
            )
            tasks.append(task)
            # store reference to the deep copy in inference_results
            inference_results.append(aiconfig_deep_copy)

        # Wait for all tasks to complete
        await asyncio.gather(*tasks)
        # Return the results. We don't need to store the results of gather, we've already stored refrences to the AIConfigRuntime objects in inference_results.
        # Each object in this list corresponds to the aiconfigruntime used in each asynchronous task.
        return inference_results

    @abstractmethod
    def get_output_text(
        self,
        prompt: Prompt,
        aiconfig: "AIConfigRuntime",
        output: Optional[Output] = None,
    ) -> str:
        """
        Get the output text from the model inference response.

        Args:
            prompt (Prompt): The prompt to be used for inference.
            aiconfig (AIConfig): The AIConfig object containing all prompts and parameters.

        Returns:
            str: The output text from the model inference response.
        """

    def get_model_settings(
        self, prompt: Prompt, aiconfig: "AIConfigRuntime"
    ) -> Dict[str, Any]:
        """
        Extracts the AI model's settings from the configuration. If both prompt and config level settings are defined, merge them with prompt settings taking precedence.

        Args:
            prompt: The prompt object.

        Returns:
            dict: The settings of the model used by the prompt.
        """
        if not prompt:
            return aiconfig.get_global_settings(self.id())

        # Check if the prompt exists in the config
        if (
            prompt.name not in aiconfig.prompt_index
            or aiconfig.prompt_index[prompt.name] != prompt
        ):
            raise IndexError(f"Prompt '{prompt.name}' not in config.")

        model_metadata = prompt.metadata.model if prompt.metadata else None

        if model_metadata is None:
            # Use Default Model
            default_model = aiconfig.get_default_model()
            if not default_model:
                raise KeyError(
                    f"No default model specified in AIConfigMetadata, and prompt `{prompt.name}` does not specify a model."
                )
            return aiconfig.get_global_settings(default_model)
        elif isinstance(model_metadata, str):
            # Use Global settings
            return aiconfig.get_global_settings(model_metadata)
        else:
            # Merge config and prompt settings with prompt settings taking precedent
            model_settings = {}
            global_settings = aiconfig.get_global_settings(model_metadata.name)
            prompt_settings = (
                prompt.metadata.model.settings
                if prompt.metadata.model.settings is not None
                else {}
            )

            model_settings.update(global_settings)
            model_settings.update(prompt_settings)

            return model_settings


def print_stream_callback(data, accumulated_data, index: int):
    """
    Default streamCallback function that prints the output to the console.
    """
    print(
        "\ndata: {}\naccumulated_data:{}\nindex:{}\n".format(
            data, accumulated_data, index
        )
    )


def print_stream_delta(data, accumulated_data, index: int):
    """
    Default streamCallback function that prints the output to the console.
    """
    if "content" in data:
        content = data["content"]
        if content:
            print(content, end="", flush=True)


class InferenceOptions:
    """
    Options that determine how to run inference for the prompt (e.g., whether to stream the output or not, callbacks, etc.)
    """

    def __init__(
        self,
        stream_callback: Callable[[Any, Any, int], Any] = print_stream_delta,
        stream=True,
        **kwargs,
    ):
        super().__init__()

        """ 
        Called when a model is in streaming mode and an update is available.

        Args:
            data: The new data chunk from the stream.
            accumulatedData: The running sum of all data chunks received so far.
            index (int): The index of the choice that the data chunk belongs to
                (default is 0, but if the model generates multiple choices, this will be the index of
                the choice that the data chunk belongs to).

            Returns:
                None
        """
        self.stream_callback = stream_callback

        self.stream = stream

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update_stream_callback(self, callback: Callable[[Any, Any, int], Any]):
        """
        Update the streamCallback function in the callbacks dictionary.
        """
        self.stream_callback = callback
