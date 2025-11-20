# 🚀 Briefcase AI Telemetry SDK - Examples & Integration Guide

[![License: BSL 1.1](https://img.shields.io/badge/License-BSL%201.1-blue.svg)](https://mariadb.com/bsl11/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Private Beta](https://img.shields.io/badge/Status-Private%20Beta-orange.svg)](mailto:support@briefcasebrain.com)

**Welcome to the Briefcase AI Telemetry SDK Examples Repository!**

This repository provides comprehensive examples, integration guides, and documentation for the **Briefcase AI Telemetry SDK** - an enterprise-grade observability platform designed specifically for AI/ML applications, LLM monitoring, cost tracking, and performance optimization.

---

## 🎯 **What is Briefcase AI Telemetry SDK?**

The **Briefcase AI Telemetry SDK** is a comprehensive observability platform built for modern AI applications. Whether you're building chatbots, running ML pipelines, or managing complex AI agent systems, our SDK provides the tools you need to monitor, optimize, and scale with confidence.

### **🌟 Core Capabilities**

| Feature | Description | Business Value |
|---------|-------------|----------------|
| **🤖 AI/ML Monitoring** | Track model performance, latency, and accuracy in real-time | Ensure AI reliability and performance |
| **💰 Cost Optimization** | Monitor and optimize AI API costs across providers | Reduce AI expenses by 20-40% |
| **📊 Drift Detection** | Detect when models deviate from expected behavior | Prevent AI degradation and failures |
| **🔍 Agent Instrumentation** | Track AI agent behaviors, decisions, and outcomes | Optimize agent performance and reliability |
| **🛡️ Compliance Tracking** | Monitor AI usage for regulatory compliance | Meet enterprise governance requirements |
| **⚡ Real-time Analytics** | Live dashboards with instant insights | Make data-driven decisions quickly |

### **🏢 Enterprise Features**

- **🔒 SOC 2 Type II Compliance** - Enterprise security standards
- **🌐 Multi-Cloud Support** - Works across AWS, GCP, Azure, and on-premises
- **📈 Auto-scaling** - Handles millions of events per day
- **🔐 Zero PII Collection** - Privacy-first design
- **🎯 Custom Metrics** - Track business-specific KPIs
- **📱 Mobile & Web SDKs** - Cross-platform monitoring

---

## 🚀 **Quick Start Guide**

### **Step 1: Join the Beta Program**

**⚠️ This SDK is currently in private beta** with limited access for select organizations.

**To request beta access:**

1. **📧 Contact us**: [support@briefcasebrain.com](mailto:support@briefcasebrain.com)
2. **📋 Provide details**:
   ```
   Subject: Beta Access Request - [Your Company]

   Organization: [Company Name]
   Use Case: [Brief description of your AI application]
   Scale: [Expected events/day or users]
   Technical Contact: [Name & Email]
   Timeline: [When you'd like to start]
   ```
3. **⏱️ Wait for approval**: 1-2 business days
4. **📄 Sign agreement**: Receive and sign Beta Participation Agreement
5. **🔑 Get credentials**: Receive API key and private PyPI access

### **Step 2: Installation (Beta Participants Only)**

Once you have beta access credentials:

```bash
# Install from private PyPI repository
pip install --index-url https://USERNAME:PASSWORD@pypi.briefcasebrain.com/simple/ briefcase-ai-telemetry

# Verify installation
python -c "import briefcase_ai_telemetry as bt; print('✅ Briefcase AI SDK Ready!')"
```

### **Step 3: Basic Integration**

```python
import briefcase_ai_telemetry as bt
import os

# Initialize telemetry client
client = bt.create_client(
    api_key=os.getenv("BRIEFCASE_API_KEY"),
    enabled=True,
    batch_size=100,
    flush_interval_seconds=30
)

# Start background telemetry
client.start_background_flush()

# Track your first AI event
event = bt.create_event(
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

client.track_event(event)
print("🎉 Your first telemetry event sent!")
```

### **Step 4: View Your Data**

Access your telemetry dashboard at: **[https://observe.briefcasebrain.io/](https://observe.briefcasebrain.io/)**

---

## 📚 **Comprehensive Examples**

### **🎓 Learning Path**

**Beginner:**
1. **[Basic Usage](examples/basic_usage.py)** - Start here for simple integration
2. **[FastAPI Integration](examples/fastapi_example.py)** - Web API monitoring
3. **[Multi-Model Chat](examples/multi_model_chat.py)** - LLM comparison and tracking

**Intermediate:**
4. **[Cost Optimization](examples/cost_optimization_tool.py)** - Reduce AI expenses
5. **[HuggingFace Integration](examples/huggingface_example.py)** - Model serving monitoring
6. **[Drift Detection](examples/drift_detection_system.py)** - ML performance monitoring

**Advanced:**
7. **[Agent Instrumentation](examples/agent_instrumentation.py)** - AI agent tracking
8. **[Compliance Framework](examples/compliance_framework_example.py)** - Enterprise governance
9. **[End-to-End Demo Notebook](examples/end_to_end_demo.ipynb)** - Complete tutorial

### **📊 Examples by Use Case**

| Use Case | Examples | Key Features |
|----------|----------|--------------|
| **Web Applications** | [FastAPI](examples/fastapi_example.py), [Flask](#), [Django](#) | Request tracking, error monitoring, performance metrics |
| **Chat Applications** | [Multi-Model Chat](examples/multi_model_chat.py), [Agent Instrumentation](examples/agent_instrumentation.py) | LLM cost tracking, conversation analytics, user behavior |
| **ML Pipelines** | [Drift Detection](examples/drift_detection_system.py), [HuggingFace](examples/huggingface_example.py) | Model monitoring, performance tracking, data quality |
| **Enterprise AI** | [Compliance Framework](examples/compliance_framework_example.py), [Cost Optimization](examples/cost_optimization_tool.py) | Governance, cost control, audit trails |

---

## 🔧 **Installation Options**

### **Method 1: Direct Installation (Recommended)**
```bash
pip install --index-url https://USERNAME:PASSWORD@pypi.briefcasebrain.com/simple/ briefcase-ai-telemetry
```

### **Method 2: Requirements File**
Create `requirements.txt`:
```txt
--index-url https://pypi.briefcasebrain.com/simple/
--trusted-host pypi.briefcasebrain.com

briefcase-ai-telemetry>=0.1.0
```

Install:
```bash
pip install -r requirements.txt
```

### **Method 3: Poetry**
```toml
[tool.poetry.dependencies]
briefcase-ai-telemetry = {version = ">=0.1.0", source = "briefcase-pypi"}

[[tool.poetry.source]]
name = "briefcase-pypi"
url = "https://pypi.briefcasebrain.com/simple/"
```

### **Method 4: Docker**
```dockerfile
FROM python:3.11-slim

# Install from private PyPI
RUN pip install --index-url https://USERNAME:PASSWORD@pypi.briefcasebrain.com/simple/ briefcase-ai-telemetry

COPY . /app
WORKDIR /app
```

---

## 🎮 **Interactive Learning**

### **📖 Documentation Guides**

| Guide | Description | Time |
|-------|-------------|------|
| **[Getting Started](GETTING_STARTED.md)** | Complete setup and first steps | 15 min |
| **[Integration Guide](INTEGRATION_GUIDE.md)** | Framework-specific examples | 30 min |
| **[Jupyter Demo](examples/end_to_end_demo.ipynb)** | Interactive hands-on tutorial | 45 min |

### **🏃‍♂️ Quick Start Tutorials**

**5-Minute Setup:**
```bash
# 1. Install (with your credentials)
pip install --index-url https://USER:PASS@pypi.briefcasebrain.com/simple/ briefcase-ai-telemetry

# 2. Set API key
export BRIEFCASE_API_KEY="your-api-key-here"

# 3. Run basic example
python examples/basic_usage.py

# 4. View dashboard
open https://observe.briefcasebrain.io/
```

**Framework-Specific Quickstarts:**
- **FastAPI**: `python examples/fastapi_example.py` → http://localhost:8000
- **Jupyter**: Open `examples/end_to_end_demo.ipynb`
- **Chat App**: `python examples/multi_model_chat.py`

---

## 🏗️ **Architecture & Technical Details**

### **🔧 System Requirements**

| Component | Requirement | Notes |
|-----------|-------------|-------|
| **Python** | 3.9+ (3.11 recommended) | Full typing support |
| **Platforms** | Linux, macOS, Windows | Native wheels available |
| **Memory** | 50MB+ available RAM | For batching and buffering |
| **Network** | HTTPS egress to `*.briefcasebrain.io` | For telemetry transmission |
| **Dependencies** | Minimal (see below) | Lightweight integration |

### **📦 Core Dependencies**

```python
# Core dependencies (automatically installed)
pydantic>=2.0.0        # Data validation
httpx>=0.24.0          # HTTP client
orjson>=3.8.0          # Fast JSON serialization
python-dateutil>=2.8.0 # Date handling
```

### **⚡ Performance Characteristics**

| Metric | Value | Notes |
|--------|-------|-------|
| **Overhead** | <5ms per event | When using batching |
| **Memory** | <10MB steady state | Configurable batch size |
| **Throughput** | 100k+ events/sec | With proper configuration |
| **Latency** | <50ms to dashboard | Real-time data pipeline |
| **Reliability** | 99.9% delivery | Automatic retries |

### **🔧 Configuration Options**

```python
# Production configuration
client = bt.create_client(
    api_key=os.getenv("BRIEFCASE_API_KEY"),
    endpoint="https://observe.briefcasebrain.io/api/v1/telemetry",
    enabled=True,

    # Performance tuning
    batch_size=1000,              # Events per batch
    flush_interval_seconds=60,    # Max time before flush
    max_retries=3,                # Retry failed requests
    timeout_seconds=30,           # Request timeout

    # Development options
    debug=False,                  # Enable debug logging
    validate_events=True          # Validate event schemas
)
```

---

## 📊 **Dashboard & Analytics**

### **🎛️ Real-time Dashboard**

Access your telemetry dashboard: **[https://observe.briefcasebrain.io/](https://observe.briefcasebrain.io/)**

**Dashboard Features:**
- **📈 Live Metrics** - Real-time event streams and KPIs
- **💰 Cost Analytics** - AI spending breakdown by model/provider
- **🔍 Event Explorer** - Search and filter telemetry events
- **📊 Custom Dashboards** - Build your own visualizations
- **🚨 Alerting** - Set up alerts for anomalies
- **📱 Mobile Responsive** - Monitor on any device

### **📈 Key Metrics Tracked**

| Category | Metrics | Use Cases |
|----------|---------|-----------|
| **Performance** | Latency, throughput, success rate | SLA monitoring, optimization |
| **Cost** | Token usage, API costs, cost per user | Budget management, optimization |
| **Quality** | Model accuracy, drift scores, errors | Model performance, reliability |
| **Usage** | Active users, feature adoption, trends | Product analytics, planning |

### **🔔 Alerting & Monitoring**

Set up alerts for:
- **💸 Cost spikes** - When AI spending exceeds thresholds
- **🐌 Performance degradation** - When latency increases
- **🚨 Error rates** - When failure rates spike
- **📉 Model drift** - When AI performance degrades
- **👥 Usage anomalies** - Unusual traffic patterns

---

## 🛡️ **Security & Compliance**

### **🔒 Security Features**

| Feature | Implementation | Benefit |
|---------|----------------|---------|
| **Data Encryption** | TLS 1.3 in transit, AES-256 at rest | Protect sensitive data |
| **API Authentication** | HMAC-signed requests with API keys | Secure access control |
| **PII Protection** | Automatic PII detection and masking | Privacy compliance |
| **Access Controls** | Role-based dashboard access | Team security |
| **Audit Logs** | Complete activity tracking | Compliance requirements |

### **📋 Compliance Standards**

- **✅ SOC 2 Type II** - Security and availability controls
- **✅ GDPR** - Data protection and privacy rights
- **✅ CCPA** - California privacy compliance
- **✅ HIPAA** - Healthcare data protection (with BAA)
- **✅ ISO 27001** - Information security management

### **🚫 Data Collection Policy**

**We DO NOT collect:**
- Personal Identifiable Information (PII)
- User passwords or credentials
- Private business data (without explicit consent)
- Raw model inputs/outputs (only metadata)

**We DO collect:**
- Performance metrics (latency, success rates)
- Usage statistics (API calls, feature usage)
- Error information (anonymized stack traces)
- Cost data (token usage, API charges)

---

## 🤝 **Beta Program Details**

### **📋 Beta Participation Requirements**

**To join the beta program, you must:**

1. **📄 Legal Agreement** - Sign the Beta Participation Agreement
2. **🏢 Valid Organization** - Represent a legitimate business or research institution
3. **🎯 Clear Use Case** - Have a specific AI application to monitor
4. **👥 Technical Contact** - Designate someone for integration support
5. **📊 Usage Commitment** - Commit to providing feedback on the platform

### **✨ Beta Program Benefits**

| Benefit | Description | Value |
|---------|-------------|-------|
| **🆓 Free Access** | No charges during beta period | $500+/month value |
| **🛠️ Direct Support** | Email and video call support | Premium support |
| **🚀 Early Features** | Access to new features first | Competitive advantage |
| **💰 Future Discounts** | Preferential pricing post-beta | 25% discount |
| **🏆 Case Study** | Optional co-marketing opportunities | Brand exposure |

### **📊 What We Need from Beta Participants**

- **📝 Monthly feedback** - Brief survey about your experience
- **🐛 Bug reports** - Help us identify and fix issues
- **💡 Feature requests** - Tell us what capabilities you need
- **📈 Usage data** - Anonymous metrics to improve performance
- **🎤 Optional testimonials** - Share your success stories

### **⏰ Beta Timeline**

| Phase | Duration | Focus | Participants |
|-------|----------|--------|--------------|
| **Phase 1** | Months 1-2 | Core functionality, stability | 5-10 organizations |
| **Phase 2** | Months 3-4 | Advanced features, integrations | 15-25 organizations |
| **Phase 3** | Months 5-6 | Performance, enterprise features | 30-50 organizations |
| **GA Launch** | Month 7 | Public availability | Open to all |

---

## 🆘 **Support & Resources**

### **📞 Getting Help**

| Contact Method | Use Case | Response Time |
|----------------|----------|---------------|
| **📧 Email**: [support@briefcasebrain.com](mailto:support@briefcasebrain.com) | All inquiries, beta access | 4-24 hours |
| **📱 Emergency**: Mentioned in beta onboarding | Critical production issues | 2-4 hours |
| **📚 Documentation**: This repository | Self-service help | Immediate |

### **🔍 Troubleshooting Guide**

**Common Issues & Solutions:**

| Issue | Cause | Solution |
|-------|-------|----------|
| **Import error** | SDK not installed | Verify beta credentials and PyPI access |
| **Events not appearing** | API key invalid | Check `BRIEFCASE_API_KEY` environment variable |
| **High latency** | Large batch size | Reduce `batch_size` in client config |
| **Memory usage** | Too many buffered events | Reduce `flush_interval_seconds` |
| **Connection errors** | Network/firewall | Ensure HTTPS access to `*.briefcasebrain.io` |

**Self-Diagnosis Commands:**
```bash
# Check SDK installation
python -c "import briefcase_ai_telemetry; print('SDK OK')"

# Test connectivity
curl -s https://observe.briefcasebrain.io/health

# Validate API key
python -c "import os; print('API Key:', 'SET' if os.getenv('BRIEFCASE_API_KEY') else 'MISSING')"
```

### **📚 Additional Resources**

- **📖 [Getting Started Guide](GETTING_STARTED.md)** - Step-by-step setup
- **🔧 [Integration Guide](INTEGRATION_GUIDE.md)** - Framework examples
- **💻 [Example Applications](examples/)** - Real-world implementations
- **🎓 [Interactive Tutorial](examples/end_to_end_demo.ipynb)** - Hands-on learning
- **📊 [Dashboard Tour](https://observe.briefcasebrain.io/docs/dashboard)** - UI walkthrough

---

## 🎯 **Success Stories & Use Cases**

### **🏢 Enterprise Use Cases**

**Financial Services:**
- Monitor LLM-powered customer service chatbots
- Track model drift in fraud detection systems
- Optimize costs across multiple AI providers

**Healthcare:**
- Ensure HIPAA compliance for AI diagnostic tools
- Monitor model performance in clinical decision support
- Track costs for medical image analysis

**E-commerce:**
- Optimize recommendation engine performance
- Monitor search and personalization models
- Track AI-powered customer support costs

**Technology:**
- Monitor developer tools and code assistants
- Track model performance in autonomous systems
- Optimize multi-model AI workflows

### **📈 Typical Results**

| Metric | Improvement | Timeline |
|--------|-------------|----------|
| **Cost Reduction** | 20-40% lower AI bills | 30-60 days |
| **Performance** | 15-30% faster response times | 14-30 days |
| **Reliability** | 99.5%+ uptime for AI services | 7-14 days |
| **Visibility** | 100% AI operations monitored | 1-7 days |

---

## 🚀 **Get Started Today**

### **Ready to Transform Your AI Observability?**

**1. Request Beta Access**
```bash
# Send email to join beta program
echo "Subject: Beta Access Request - [Your Company]" | mail support@briefcasebrain.com
```

**2. Explore Examples**
```bash
# Clone this repository
git clone https://github.com/briefcasebrain/telemetry-sdk-examples.git
cd telemetry-sdk-examples

# Browse examples
ls examples/
```

**3. Join the Community**
- **📧 Email**: [support@briefcasebrain.com](mailto:support@briefcasebrain.com)
- **🌟 Star this repo**: Help others discover Briefcase AI
- **🍴 Fork and experiment**: Try the examples in your environment

---

## ⚖️ **Legal & Licensing**

### **📄 License**
Licensed under the **Business Source License 1.1**
- ✅ **Free for development and testing**
- ✅ **Free for non-commercial use**
- 💼 **Commercial licenses available** - Contact [support@briefcasebrain.com](mailto:support@briefcasebrain.com)

### **🔒 Privacy & Terms**
- **Beta Participation Agreement** required for SDK access
- **Data Processing Agreement** available for enterprise customers
- **Privacy Policy**: No PII collection by design
- **Liability Cap**: Limited to $100 USD during beta period

---

**🎉 Start building the future of AI observability today!**

[![Get Started](https://img.shields.io/badge/Get%20Started-Join%20Beta-blue.svg)](mailto:support@briefcasebrain.com?subject=Beta%20Access%20Request)
[![View Dashboard](https://img.shields.io/badge/View-Dashboard-green.svg)](https://observe.briefcasebrain.io/)
[![Documentation](https://img.shields.io/badge/Read-Docs-orange.svg)](GETTING_STARTED.md)

**Questions? We're here to help!**
📧 [support@briefcasebrain.com](mailto:support@briefcasebrain.com)