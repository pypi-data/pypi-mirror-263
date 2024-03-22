import grpc

import proto.dtx.services.prompts.v1.prompts_pb2 as prompts_pb2
import proto.dtx.services.prompts.v1.prompts_pb2_grpc as prompts_pb2_grpc
import proto.dtx.messages.common.llm_pb2 as llm_pb2

import google.protobuf.empty_pb2 as empty_pb2

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

class PromptService:
    """
    Wrap the gRPC stub with a more Pythonic interface
    """
    def __init__(self, channel: grpc.Channel):
        self.stub = prompts_pb2_grpc.PromptServiceStub(channel)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=5), retry=retry_if_exception_type(grpc.RpcError))
    def ping(self) -> None:
        """
        Ping the service to verify connectivity and authentication
        """
        self.stub.Ping(empty_pb2.Empty())

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=5), retry=retry_if_exception_type(grpc.RpcError))
    def generate_prompt(self, count: int, timeout=5) -> prompts_pb2.PromptGenerationResponse:
        """
        Generate a prompt
        """
        return self.stub.GeneratePrompts(prompts_pb2.PromptGenerationRequest(count=count), timeout=timeout)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=5), retry=retry_if_exception_type(grpc.RpcError))
    def evaluate_prompt_response(self,
                                 prompt: prompts_pb2.Prompt,
                                 model_response: str,
                                 timeout=30,
                                 model_type=llm_pb2.LLM_EVALUATION_MODEL_TYPE_COMPREHENSIVE) -> prompts_pb2.PromptEvaluationResponse:
        """
        Evaluate a prompt response
        """
        req = prompts_pb2.PromptEvaluationRequest()
        req.prompt.CopyFrom(prompt)
        req.responses.extend([prompts_pb2.PromptResponse(message=llm_pb2.LlmChatIo(content=model_response))])
        req.model_type = model_type

        return self.stub.EvaluateModelInteraction(req, timeout=timeout)


def get_prompts_service(channel: grpc.Channel) -> PromptService:
    """
    Return a gRPC stub for the PromptsService
    """
    return PromptService(channel)


