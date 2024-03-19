from censius.endpoint import get_gateway_url, get_gateway_llm_url


LLM_REGISTER_DATASET_URL = (
    lambda project_id: f"{get_gateway_url()}/{project_id}/res/nlp-input-training/frd/v1/llm/register_training_data"
)

LLM_REGISTER_MODEL_URL = (
    lambda project_id: f"{get_gateway_url()}/{project_id}/res/register_model/frd/api/llm/register_model"
)

LLM_REGISTER_LOGS = (
    lambda project_id: f"{get_gateway_url()}/{project_id}/res/nlp-input-logs/frd/v1/llm/register_logs"
)

BULK_CHUNK_SIZE = 2000
