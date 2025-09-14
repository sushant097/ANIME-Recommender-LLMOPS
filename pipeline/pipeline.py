from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException


logger = get_logger(__name__)


class AnimeRecommendationPipeline:
    def __init__(self):
        try:
            logger.info("AnimeRecommendationPipeline initializing..")
            vector_builder = VectorStoreBuilder(csv_path="")
            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(
                retriever=retriever,
                api_key=GROQ_API_KEY,
                model_name=MODEL_NAME
            )
            logger.info("AnimeRecommendationPipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing AnimeRecommendationPipeline: {e}")
            raise CustomException("Error initializing AnimeRecommendationPipeline", e)

    def recommend(self, user_query: str) -> str:
        try:
            logger.info(f"Received user query: {user_query}")
            recommendation = self.recommender.get_recommendation(user_query)
            logger.info("Generated recommendation successfully.")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to generate recommendation: {e}")
            raise CustomException("Error generating recommendation", e)
