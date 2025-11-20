#!/usr/bin/env python3
"""
FastAPI Integration Example for Briefcase AI Telemetry SDK

This example demonstrates how to integrate the Briefcase AI Telemetry SDK
with a FastAPI application for comprehensive API observability.

Requirements (Beta Access Required):
- pip install --index-url https://USERNAME:PASSWORD@pypi.briefcasebrain.com/simple/ briefcase-ai-telemetry
- pip install fastapi uvicorn openai

Usage:
    python fastapi_example.py
    curl http://localhost:8000/chat -d '{"message": "Hello AI!"}'
"""

import asyncio
import logging
import os
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Import Briefcase AI Telemetry (Beta Access Required)
try:
    import briefcase_ai_telemetry as bt
except ImportError:
    print("❌ Briefcase AI Telemetry SDK not found!")
    print("📋 To install: contact beta@briefcasebrain.com for access")
    print("📦 Install: pip install --index-url https://USERNAME:PASSWORD@pypi.briefcasebrain.com/simple/ briefcase-ai-telemetry")
    exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global telemetry client
telemetry_client = None

class ChatRequest(BaseModel):
    message: str
    model: str = "gpt-3.5-turbo"

class ChatResponse(BaseModel):
    response: str
    model: str
    cost_estimate: float
    processing_time: float

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for telemetry setup and teardown."""
    global telemetry_client

    # Startup: Initialize telemetry
    logger.info("🚀 Starting FastAPI with Briefcase AI Telemetry")

    api_key = os.getenv("BRIEFCASE_API_KEY")
    if not api_key:
        logger.warning("⚠️ BRIEFCASE_API_KEY not set - telemetry disabled")
        telemetry_client = bt.create_client("demo-key", enabled=False)
    else:
        telemetry_client = bt.create_client(
            api_key=api_key,
            endpoint="https://observe.briefcasebrain.io/api/v1/telemetry",
            enabled=True,
            batch_size=50,
            flush_interval_seconds=30
        )

    # Start background telemetry
    telemetry_client.start_background_flush()

    # Track application startup
    startup_event = bt.create_event(
        "fastapi_startup",
        level=bt.EventLevel.info(),
        custom_data={
            "service": "chat-api",
            "version": "1.0.0",
            "environment": os.getenv("ENVIRONMENT", "development")
        }
    )
    telemetry_client.track_event(startup_event)

    yield

    # Shutdown: Cleanup telemetry
    logger.info("🛑 Shutting down FastAPI")

    # Track application shutdown
    shutdown_event = bt.create_event(
        "fastapi_shutdown",
        level=bt.EventLevel.info(),
        custom_data={"service": "chat-api"}
    )
    telemetry_client.track_event(shutdown_event)

    # Ensure all events are sent
    await asyncio.sleep(1)

# Create FastAPI app with lifespan
app = FastAPI(
    title="Briefcase AI Chat API",
    description="Example FastAPI app with Briefcase AI Telemetry integration",
    version="1.0.0",
    lifespan=lifespan
)

async def mock_openai_call(message: str, model: str) -> Dict[str, Any]:
    """Mock OpenAI API call for demonstration purposes."""
    # Simulate API latency
    await asyncio.sleep(0.5)

    # Mock response
    response_text = f"I received your message: '{message}'. This is a mock response from {model}."

    # Mock cost calculation (varies by model)
    cost_per_token = {
        "gpt-3.5-turbo": 0.0015,
        "gpt-4": 0.03,
        "gpt-4-turbo": 0.01
    }

    estimated_tokens = len(message.split()) + len(response_text.split())
    cost = estimated_tokens * cost_per_token.get(model, 0.002)

    return {
        "response": response_text,
        "cost": cost,
        "tokens_used": estimated_tokens
    }

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Chat endpoint with comprehensive telemetry tracking."""
    import time

    start_time = time.time()
    request_id = f"req_{int(start_time * 1000)}"

    # Track request start
    request_event = bt.create_event(
        "api_request_start",
        level=bt.EventLevel.info(),
        custom_data={
            "request_id": request_id,
            "endpoint": "/chat",
            "model": request.model,
            "message_length": len(request.message)
        }
    )
    telemetry_client.track_event(request_event)

    try:
        # Simulate AI model call
        result = await mock_openai_call(request.message, request.model)
        processing_time = time.time() - start_time

        # Track successful completion
        success_event = bt.create_event(
            "ai_model_completion",
            level=bt.EventLevel.info(),
            custom_data={
                "request_id": request_id,
                "model": request.model,
                "processing_time_ms": processing_time * 1000,
                "cost_usd": result["cost"],
                "tokens_used": result["tokens_used"],
                "success": True
            }
        )
        telemetry_client.track_event(success_event)

        # Track cost optimization metrics
        cost_event = bt.create_event(
            "cost_tracking",
            level=bt.EventLevel.info(),
            custom_data={
                "request_id": request_id,
                "model": request.model,
                "cost_usd": result["cost"],
                "cost_per_token": result["cost"] / result["tokens_used"],
                "efficiency_score": result["tokens_used"] / processing_time
            }
        )
        telemetry_client.track_event(cost_event)

        return ChatResponse(
            response=result["response"],
            model=request.model,
            cost_estimate=result["cost"],
            processing_time=processing_time
        )

    except Exception as e:
        processing_time = time.time() - start_time

        # Track error
        error_event = bt.create_event(
            "api_request_error",
            level=bt.EventLevel.error(),
            custom_data={
                "request_id": request_id,
                "endpoint": "/chat",
                "error_type": type(e).__name__,
                "error_message": str(e),
                "processing_time_ms": processing_time * 1000
            }
        )
        telemetry_client.track_event(error_event)

        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint with telemetry."""
    health_event = bt.create_event(
        "health_check",
        level=bt.EventLevel.info(),
        custom_data={
            "status": "healthy",
            "telemetry_enabled": telemetry_client is not None
        }
    )
    telemetry_client.track_event(health_event)

    return {
        "status": "healthy",
        "telemetry": "enabled" if telemetry_client else "disabled",
        "service": "chat-api"
    }

@app.get("/metrics")
async def get_metrics():
    """Get basic application metrics."""
    # This would typically pull from your telemetry dashboard
    # For demo purposes, we'll return mock metrics

    metrics_event = bt.create_event(
        "metrics_requested",
        level=bt.EventLevel.info(),
        custom_data={"endpoint": "/metrics"}
    )
    telemetry_client.track_event(metrics_event)

    return {
        "total_requests": "tracked_via_telemetry",
        "average_response_time": "tracked_via_telemetry",
        "total_cost": "tracked_via_telemetry",
        "dashboard": "https://observe.briefcasebrain.io/"
    }

if __name__ == "__main__":
    print("🚀 Starting FastAPI Chat API with Briefcase AI Telemetry")
    print("📊 Dashboard: https://observe.briefcasebrain.io/")
    print("🔑 Set BRIEFCASE_API_KEY environment variable for full telemetry")
    print("📖 Example usage:")
    print("   curl http://localhost:8000/chat -X POST -H 'Content-Type: application/json' -d '{\"message\": \"Hello AI!\"}'")
    print("")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )