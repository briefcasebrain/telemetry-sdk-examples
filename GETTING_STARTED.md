# 🚀 Getting Started with Briefcase AI Telemetry SDK

This guide helps you quickly integrate Briefcase AI Telemetry into your applications.

## 📋 Prerequisites

**⚠️ Beta Access Required**

1. **Sign Beta Agreement**: Contact [support@briefcasebrain.com](mailto:support@briefcasebrain.com)
2. **Get Credentials**: Receive API key and PyPI access
3. **Install SDK**: Access to private repository at `https://pypi.briefcasebrain.com/`

## 🔧 Installation

```bash
# Beta participants only - use provided credentials
pip install --index-url https://USERNAME:PASSWORD@pypi.briefcasebrain.com/simple/ briefcase-ai-telemetry
```

## ⚡ Quick Start

### 1. Basic Setup

```python
import briefcase_ai_telemetry as bt
import os

# Initialize client
client = bt.create_client(
    api_key=os.getenv("BRIEFCASE_API_KEY"),
    enabled=True  # Set False for local development
)

# Start background telemetry
client.start_background_flush()
```

### 2. Track Your First Event

```python
# Create and track an event
event = bt.create_event(
    "user_action",
    level=bt.EventLevel.info(),
    custom_data={
        "action": "button_click",
        "feature": "export_data",
        "duration_ms": 150
    }
)

client.track_event(event)
```

### 3. Monitor AI Model Usage

```python
# Track AI model calls
model_event = bt.create_event(
    "ai_model_call",
    level=bt.EventLevel.info(),
    custom_data={
        "model": "gpt-3.5-turbo",
        "tokens": 150,
        "cost_usd": 0.0003,
        "latency_ms": 1200,
        "success": True
    }
)

client.track_event(model_event)
```

## 📊 View Your Data

Once you start tracking events:

1. **Dashboard**: Visit [https://observe.briefcasebrain.io/](https://observe.briefcasebrain.io/)
2. **Login**: Use credentials provided during beta onboarding
3. **Monitor**: View real-time metrics, costs, and performance data

## 🎯 Next Steps

**Choose Your Integration Path:**

### **Web Applications**
- **[FastAPI Example](examples/fastapi_example.py)** - REST API monitoring
- **[Flask Integration](examples/flask_example.py)** - Web app telemetry
- **[Django Setup](examples/django_example.py)** - Full-stack monitoring

### **AI/ML Applications**
- **[Multi-Model Chat](examples/multi_model_chat.py)** - LLM cost tracking
- **[HuggingFace Integration](examples/huggingface_example.py)** - Model serving
- **[Drift Detection](examples/drift_detection_system.py)** - Performance monitoring

### **Enterprise Features**
- **[Cost Optimization](examples/cost_optimization_tool.py)** - Reduce AI expenses
- **[Compliance Framework](examples/compliance_framework_example.py)** - Governance
- **[Agent Instrumentation](examples/agent_instrumentation.py)** - AI agent tracking

### **Interactive Learning**
- **[Jupyter Notebook Demo](examples/end_to_end_demo.ipynb)** - Complete walkthrough

## 💡 Tips for Success

### **Development Best Practices**

```python
# ✅ Use environment-based configuration
client = bt.create_client(
    api_key=os.getenv("BRIEFCASE_API_KEY"),
    enabled=os.getenv("ENVIRONMENT") == "production",  # Only in prod
    batch_size=100,
    flush_interval_seconds=30
)

# ✅ Track meaningful metrics
client.track_event(bt.create_event(
    "api_request",
    level=bt.EventLevel.info(),
    custom_data={
        "endpoint": "/api/users",
        "method": "GET",
        "status_code": 200,
        "duration_ms": 45,
        "user_type": "premium"  # Avoid PII
    }
))

# ❌ Don't track sensitive data
client.track_event(bt.create_event(
    "user_login",
    level=bt.EventLevel.info(),
    custom_data={
        "email": "user@example.com",  # ❌ PII violation
        "password": "secret123"       # ❌ Security risk
    }
))
```

### **Performance Optimization**

```python
# Use batching for high-volume applications
client = bt.create_client(
    api_key=os.getenv("BRIEFCASE_API_KEY"),
    batch_size=500,               # Larger batches
    flush_interval_seconds=60,    # Less frequent flushes
    max_retries=3
)

# Track performance metrics
start_time = time.time()
# ... your code ...
duration = time.time() - start_time

client.track_event(bt.create_event(
    "performance_metric",
    level=bt.EventLevel.info(),
    custom_data={
        "operation": "data_processing",
        "duration_ms": duration * 1000,
        "records_processed": len(data)
    }
))
```

## 🆘 Need Help?

**Support Channels:**
- **📧 Support**: [support@briefcasebrain.com](mailto:support@briefcasebrain.com)

**Common Issues:**
- **Installation fails**: Verify beta credentials and repository access
- **Events not appearing**: Check API key and network connectivity
- **Performance impact**: Adjust batch size and flush intervals

## 🎯 Success Checklist

- [ ] **Beta access approved** - Agreement signed and credentials received
- [ ] **SDK installed** - Can import `briefcase_ai_telemetry`
- [ ] **API key configured** - Set `BRIEFCASE_API_KEY` environment variable
- [ ] **First event tracked** - Events appear in dashboard
- [ ] **Integration tested** - Verified in staging environment
- [ ] **Monitoring enabled** - Dashboard bookmarked and team has access

**Ready to build the future of AI observability!** 🚀