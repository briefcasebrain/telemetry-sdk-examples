# 🔧 Integration Guide - Framework Examples

Complete integration examples for popular Python frameworks.

## 🌟 **Framework Support Matrix**

| Framework | Status | Example | Use Case |
|-----------|--------|---------|----------|
| **FastAPI** | ✅ Full Support | [fastapi_example.py](examples/fastapi_example.py) | REST APIs, Microservices |
| **Flask** | ✅ Full Support | [flask_example.py](#flask-integration) | Web Applications |
| **Django** | ✅ Full Support | [django_example.py](#django-integration) | Full-Stack Apps |
| **Streamlit** | ✅ Full Support | [streamlit_example.py](#streamlit-integration) | ML Dashboards |
| **Jupyter** | ✅ Full Support | [end_to_end_demo.ipynb](examples/end_to_end_demo.ipynb) | Data Science |

---

## 🚀 **FastAPI Integration**

Complete example: [examples/fastapi_example.py](examples/fastapi_example.py)

### **Key Features**
- Application lifespan management
- Request/response tracking
- Error monitoring
- Cost optimization metrics

### **Quick Setup**

```python
from fastapi import FastAPI
import briefcase_ai_telemetry as bt

# Global telemetry client
telemetry_client = bt.create_client(
    api_key=os.getenv("BRIEFCASE_API_KEY"),
    enabled=True
)

app = FastAPI()

@app.middleware("http")
async def telemetry_middleware(request, call_next):
    start_time = time.time()

    response = await call_next(request)
    processing_time = time.time() - start_time

    # Track API request
    telemetry_client.track_event(bt.create_event(
        "api_request",
        level=bt.EventLevel.info(),
        custom_data={
            "method": request.method,
            "url": str(request.url),
            "status_code": response.status_code,
            "duration_ms": processing_time * 1000
        }
    ))

    return response
```

---

## 🌶️ **Flask Integration**

### **Complete Flask Example**

```python
from flask import Flask, request, jsonify
import briefcase_ai_telemetry as bt
import time
import functools

app = Flask(__name__)

# Initialize telemetry
telemetry_client = bt.create_client(
    api_key=os.getenv("BRIEFCASE_API_KEY"),
    enabled=True
)
telemetry_client.start_background_flush()

def track_request(f):
    """Decorator to track Flask requests."""
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        start_time = time.time()

        try:
            response = f(*args, **kwargs)
            processing_time = time.time() - start_time

            # Track successful request
            telemetry_client.track_event(bt.create_event(
                "flask_request",
                level=bt.EventLevel.info(),
                custom_data={
                    "endpoint": request.endpoint,
                    "method": request.method,
                    "duration_ms": processing_time * 1000,
                    "success": True
                }
            ))

            return response

        except Exception as e:
            processing_time = time.time() - start_time

            # Track error
            telemetry_client.track_event(bt.create_event(
                "flask_error",
                level=bt.EventLevel.error(),
                custom_data={
                    "endpoint": request.endpoint,
                    "method": request.method,
                    "duration_ms": processing_time * 1000,
                    "error": str(e)
                }
            ))
            raise

    return decorated_function

@app.route('/api/chat', methods=['POST'])
@track_request
def chat():
    data = request.get_json()
    message = data.get('message', '')

    # Simulate AI processing
    time.sleep(0.5)
    response = f"Echo: {message}"

    # Track AI usage
    telemetry_client.track_event(bt.create_event(
        "ai_chat",
        level=bt.EventLevel.info(),
        custom_data={
            "message_length": len(message),
            "response_length": len(response),
            "model": "echo-model"
        }
    ))

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🎸 **Django Integration**

### **Django Middleware Setup**

```python
# middleware.py
import time
import briefcase_ai_telemetry as bt
from django.conf import settings

class BriefcaseTelemetryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.telemetry_client = bt.create_client(
            api_key=settings.BRIEFCASE_API_KEY,
            enabled=getattr(settings, 'TELEMETRY_ENABLED', True)
        )
        self.telemetry_client.start_background_flush()

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        processing_time = time.time() - start_time

        # Track Django request
        self.telemetry_client.track_event(bt.create_event(
            "django_request",
            level=bt.EventLevel.info(),
            custom_data={
                "path": request.path,
                "method": request.method,
                "status_code": response.status_code,
                "duration_ms": processing_time * 1000,
                "user_authenticated": request.user.is_authenticated
            }
        ))

        return response

# settings.py
MIDDLEWARE = [
    'myapp.middleware.BriefcaseTelemetryMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # ... other middleware
]

BRIEFCASE_API_KEY = os.getenv('BRIEFCASE_API_KEY')
TELEMETRY_ENABLED = os.getenv('ENVIRONMENT') == 'production'
```

### **Django View Example**

```python
# views.py
from django.shortcuts import render
from django.http import JsonResponse
import briefcase_ai_telemetry as bt

def ai_chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        # Track AI interaction
        telemetry_client = bt.create_client(
            api_key=settings.BRIEFCASE_API_KEY,
            enabled=True
        )

        telemetry_client.track_event(bt.create_event(
            "ai_chat_django",
            level=bt.EventLevel.info(),
            custom_data={
                "message_length": len(message),
                "view": "ai_chat_view",
                "user_id": request.user.id if request.user.is_authenticated else None
            }
        ))

        # Simulate AI processing
        response = f"Django AI Response: {message}"

        return JsonResponse({"response": response})

    return render(request, 'chat.html')
```

---

## 📊 **Streamlit Integration**

### **Streamlit Dashboard Example**

```python
# streamlit_telemetry_app.py
import streamlit as st
import briefcase_ai_telemetry as bt
import time
import pandas as pd

# Initialize telemetry in session state
if 'telemetry_client' not in st.session_state:
    st.session_state.telemetry_client = bt.create_client(
        api_key=st.secrets["BRIEFCASE_API_KEY"],
        enabled=True
    )
    st.session_state.telemetry_client.start_background_flush()

def track_streamlit_event(event_name, custom_data=None):
    """Helper function to track Streamlit events."""
    st.session_state.telemetry_client.track_event(bt.create_event(
        event_name,
        level=bt.EventLevel.info(),
        custom_data=custom_data or {}
    ))

# Streamlit app
st.title("🚀 AI Dashboard with Telemetry")

# Track page view
track_streamlit_event("page_view", {"page": "dashboard"})

# AI Model Selection
model = st.selectbox(
    "Choose AI Model:",
    ["gpt-3.5-turbo", "gpt-4", "claude-3-sonnet"]
)

# Track model selection
if st.button("Select Model"):
    track_streamlit_event("model_selected", {"model": model})
    st.success(f"Selected: {model}")

# Chat Interface
user_input = st.text_input("Enter your message:")

if st.button("Send") and user_input:
    start_time = time.time()

    # Simulate AI processing
    time.sleep(1)
    response = f"AI ({model}): I received '{user_input}'"

    processing_time = time.time() - start_time

    # Track AI interaction
    track_streamlit_event("ai_interaction", {
        "model": model,
        "input_length": len(user_input),
        "processing_time_ms": processing_time * 1000,
        "success": True
    })

    st.write(f"**Response:** {response}")

# Display metrics
if st.button("Show Telemetry Stats"):
    track_streamlit_event("metrics_viewed", {"component": "stats_panel"})

    # Mock telemetry data
    st.subheader("📊 Telemetry Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Interactions", "1,234")

    with col2:
        st.metric("Average Response Time", "1.2s")

    with col3:
        st.metric("Total Cost", "$45.67")

    # Chart example
    data = pd.DataFrame({
        'Time': pd.date_range('2024-01-01', periods=10, freq='D'),
        'Requests': [10, 15, 13, 17, 20, 25, 22, 30, 28, 35]
    })

    st.line_chart(data.set_index('Time'))
```

---

## 🔧 **Advanced Integration Patterns**

### **1. Custom Decorators**

```python
import functools
import time

def track_function(event_name):
    """Decorator to track function execution."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()

            try:
                result = func(*args, **kwargs)
                duration = time.time() - start_time

                telemetry_client.track_event(bt.create_event(
                    event_name,
                    level=bt.EventLevel.info(),
                    custom_data={
                        "function": func.__name__,
                        "duration_ms": duration * 1000,
                        "success": True,
                        "args_count": len(args),
                        "kwargs_count": len(kwargs)
                    }
                ))

                return result

            except Exception as e:
                duration = time.time() - start_time

                telemetry_client.track_event(bt.create_event(
                    f"{event_name}_error",
                    level=bt.EventLevel.error(),
                    custom_data={
                        "function": func.__name__,
                        "duration_ms": duration * 1000,
                        "error": str(e),
                        "error_type": type(e).__name__
                    }
                ))
                raise

        return wrapper
    return decorator

# Usage
@track_function("data_processing")
def process_large_dataset(data):
    # Your processing logic
    time.sleep(2)  # Simulate work
    return {"processed": len(data)}
```

### **2. Context Managers**

```python
from contextlib import contextmanager
import time

@contextmanager
def track_operation(operation_name, **context_data):
    """Context manager for tracking operations."""
    start_time = time.time()

    try:
        yield

        duration = time.time() - start_time
        telemetry_client.track_event(bt.create_event(
            operation_name,
            level=bt.EventLevel.info(),
            custom_data={
                **context_data,
                "duration_ms": duration * 1000,
                "success": True
            }
        ))

    except Exception as e:
        duration = time.time() - start_time
        telemetry_client.track_event(bt.create_event(
            f"{operation_name}_error",
            level=bt.EventLevel.error(),
            custom_data={
                **context_data,
                "duration_ms": duration * 1000,
                "error": str(e)
            }
        ))
        raise

# Usage
with track_operation("database_query", table="users", operation="SELECT"):
    # Database operation
    results = db.execute("SELECT * FROM users")
```

### **3. Async Support**

```python
import asyncio
import time

async def track_async_function(func, event_name, **context_data):
    """Track async function execution."""
    start_time = time.time()

    try:
        result = await func()
        duration = time.time() - start_time

        telemetry_client.track_event(bt.create_event(
            event_name,
            level=bt.EventLevel.info(),
            custom_data={
                **context_data,
                "duration_ms": duration * 1000,
                "success": True
            }
        ))

        return result

    except Exception as e:
        duration = time.time() - start_time

        telemetry_client.track_event(bt.create_event(
            f"{event_name}_error",
            level=bt.EventLevel.error(),
            custom_data={
                **context_data,
                "duration_ms": duration * 1000,
                "error": str(e)
            }
        ))
        raise

# Usage
async def ai_model_call():
    await asyncio.sleep(1)  # Simulate AI call
    return "AI response"

result = await track_async_function(
    ai_model_call,
    "async_ai_call",
    model="gpt-4"
)
```

---

## 🎯 **Best Practices**

### **✅ Do's**
- Use environment variables for configuration
- Track meaningful business metrics
- Implement proper error handling
- Use batching for high-volume applications
- Monitor telemetry overhead

### **❌ Don'ts**
- Don't track PII or sensitive data
- Don't block application flow for telemetry
- Don't track every minor operation
- Don't ignore telemetry errors
- Don't forget to test in staging

### **🔧 Configuration Examples**

```python
# Production configuration
telemetry_client = bt.create_client(
    api_key=os.getenv("BRIEFCASE_API_KEY"),
    enabled=os.getenv("ENVIRONMENT") == "production",
    batch_size=1000,
    flush_interval_seconds=60,
    max_retries=3
)

# Development configuration
telemetry_client = bt.create_client(
    api_key="dev-key",
    enabled=False,  # Disabled in development
    batch_size=10,
    flush_interval_seconds=5
)
```

---

## 🆘 **Troubleshooting**

### **Common Issues**

**Events not appearing in dashboard:**
- Verify API key is correct
- Check network connectivity
- Ensure `enabled=True` in production
- Verify events are being created properly

**Performance impact:**
- Increase `batch_size` (default: 100)
- Increase `flush_interval_seconds` (default: 30)
- Use async/background processing
- Monitor telemetry overhead

**Integration errors:**
- Check framework compatibility
- Verify import statements
- Test with minimal example first
- Check for dependency conflicts

Ready to integrate? Choose your framework and start building! 🚀