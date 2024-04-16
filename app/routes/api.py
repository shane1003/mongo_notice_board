from fastapi import APIRouter
from app.routes import user, article, register, auth

router = APIRouter()
router.include_router(user.router, tags=["account"], prefix="/account")
router.include_router(article.router, tags=["article"], prefix="/article")
router.include_router(register.router, tags=["register"], prefix="/register")
router.include_router(auth.router, tags=["Authentication"])