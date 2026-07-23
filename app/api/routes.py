from fastapi import APIRouter, HTTPException, status

from app.api.schemas import (
    ChatRequest,
    ChatResponse,
)

from app.services.recommendation_service import recommend

router = APIRouter()


# --------------------------------------------------
# Root
# --------------------------------------------------

@router.get("/")
def root():

    return {
        "message": "Welcome to Weeber API 🚀",
        "docs": "/docs",
        "health": "/health"
    }


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@router.get("/health")
def health():

    return {
        "status": "healthy"
    }


# --------------------------------------------------
# Chat Endpoint
# --------------------------------------------------

@router.post(
    "/recommend",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
)
def chat(request: ChatRequest):

    query = request.query.strip()

    if not query:

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail="Query cannot be empty."

        )

    try:

        result = recommend(query)

        return result

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(

            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            detail=f"Internal Server Error: {str(e)}"

        )