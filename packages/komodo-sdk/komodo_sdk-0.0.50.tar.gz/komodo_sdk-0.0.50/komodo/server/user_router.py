from fastapi import APIRouter, Depends

from komodo.loaders.user_loader import UserLoader
from komodo.server.globals import get_email_from_header, get_appliance

router = APIRouter(
    prefix='/api/v1/user',
    tags=['User']
)


@router.get("/profile", response_model=dict, summary="Get user profile.", description="Get user profile.")
async def get_user_profile(email: str = Depends(get_email_from_header), appliance=Depends(get_appliance)):
    user = UserLoader.load(email) or next((x for x in appliance.users if x.email == email), None)
    return user.to_dict() if user else {"error": "User not found."}
