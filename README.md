# 🤖 Automated PR Review: Your AI-Powered Code Guardian

> _"Where human insight meets artificial intelligence to craft exceptional code"_

## ✨ The Vision

In the fast-paced world of software development, code reviews are the gatekeepers of quality. But what if we could amplify human expertise with the precision of AI? **Automated PR Review** transforms the traditional code review process into an intelligent, responsive system that never sleeps, never misses a detail, and always has your back.

Powered by **Claude 3.5 Sonnet**, this revolutionary tool doesn't just scan your code—it _understands_ it. From subtle logic flaws to optimization opportunities, from complexity analysis to thoughtful suggestions, your new AI reviewer brings enterprise-grade intelligence to every pull request.

## 🎯 **See It In Action**

Here's a real example of our AI reviewer analyzing code changes with detailed feedback (If needed, we can restrict the number of words to 100, if the feedback need to be crisp):

<div align="center">
  <img src="assets/automated_pr_comment.png" alt="Automated PR Review in Action" width="700"/>
  <p><em>✨ Real AI review showing complexity analysis, code suggestions, and encouraging feedback</em></p>
</div>

As you can see, the AI reviewer provides:

- ✅ **Comprehensive checklist validation** (Time/Space complexity, documentation)
- 🔍 **Detailed code analysis** with specific improvement suggestions
- 📊 **Performance insights** and optimization recommendations
- 🎉 **Positive reinforcement** with creative compliments like "Pristine!"

## 🚀 What Makes This Special?

### 🎯 **Intelligent Analysis**

- **Logic & Implementation Review**: Spots potential bugs before they reach production
- **Performance Insights**: Analyzes time and space complexity with precision
- **Best Practices Enforcement**: Ensures your code follows industry standards
- **Constructive Feedback**: Actionable suggestions that make you a better developer

### ⚡ **Seamless Integration**

- **GitHub Webhook Magic**: Automatically triggers on every PR
- **Zero Configuration Overhead**: Set it once, forget about it forever
- **Real-time Responses**: Get instant feedback the moment you open a PR
- **Non-intrusive Design**: Enhances your workflow without disrupting it

### 🎨 **Human-Centered Experience**

- **Encouraging Tone**: Celebrates good code with creative compliments
- **Developer-Friendly**: Comments only on what matters in the diff
- **Quality Checklist**: Ensures documentation and complexity analysis
- **Smart Filtering**: Ignores noise, focuses on substance

## 🏗️ Architecture That Scales

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GitHub PR     │───▶│   FastAPI App    │───▶│   Claude 3.5    │
│   Webhook       │    │   (main.py)      │    │   Sonnet API    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   Smart Review   │
                       │   Comment        │
                       └──────────────────┘
```

**Built with Modern Stack:**

- 🚀 **FastAPI**: Lightning-fast async web framework
- 🧠 **Claude 3.5 Sonnet**: State-of-the-art language model
- 🐙 **GitHub API**: Seamless repository integration
- 📦 **Pydantic**: Type-safe data validation
- 🔄 **HTTPX**: Modern async HTTP client

## 🛠️ Quick Start Guide

### Prerequisites

- Python 3.8+
- GitHub repository with admin access
- Anthropic API key
- GitHub Personal Access Token

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/automated-pr-review.git
   cd automated-pr-review
   ```

2. **Set up your environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure your secrets**

   ```bash
   export ANTHROPIC_API_KEY="your-anthropic-api-key"
   export GITHUB_TOKEN="your-github-token"
   ```

4. **Launch the application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### 🚀 Automated Deployment with GitHub Actions

The project includes a complete CI/CD pipeline that automatically:

- ✅ **Runs tests** on every push and PR
- 🐳 **Builds Docker image** and pushes to GitHub Container Registry
- 🌐 **Deploys to cloud** platforms automatically on main branch

#### Required GitHub Secrets

Add these secrets to your repository (Settings → Secrets and variables → Actions):

```bash
ANTHROPIC_API_KEY=your-anthropic-api-key
GITHUB_TOKEN=automatically-provided
# Optional: Add secrets for your chosen cloud provider
RAILWAY_TOKEN=your-railway-token
RENDER_API_KEY=your-render-api-key
HEROKU_APP_NAME=your-heroku-app-name
```

#### Deployment Options

The workflow supports multiple cloud platforms:

- 🌊 **Google Cloud Run** (recommended for enterprise)
- 🚂 **Railway** (great for startups)
- 🎨 **Render** (developer-friendly)
- 💜 **Heroku** (classic choice)
- Currently it is deployed in Railway

Simply uncomment your preferred deployment section in `.github/workflows/deploy.yml`

### 📖 **Live API Documentation**

🌐 **Try the API directly**: [https://automated-pr-review-production.up.railway.app/docs](https://automated-pr-review-production.up.railway.app/docs)

Explore the interactive Swagger documentation to understand the webhook endpoint structure and test API calls directly in your browser.

### Manual Deployment with Docker

```bash
# Build the image
docker build -t automated-pr-review .

# Run locally
docker run -p 8000:8000 \
  -e ANTHROPIC_API_KEY=your-key \
  -e GITHUB_TOKEN=your-token \
  automated-pr-review
```

### GitHub Webhook Setup

1. Navigate to your repository → Settings → Webhooks
2. Click "Add webhook"
3. Set payload URL to `https://your-deployed-domain.com/webhook`
4. Content type: `application/json`
5. Select "Pull requests" events
6. Save and celebrate! 🎉

## 🎯 Core Features

### **Smart Code Analysis**

The AI reviewer examines your code with the precision of a senior engineer:

- **Bug Detection**: Identifies potential runtime errors and edge cases
- **Performance Review**: Analyzes algorithmic complexity and optimization opportunities
- **Code Quality**: Ensures readability, maintainability, and best practices
- **Documentation Check**: Validates that complex logic includes proper explanations

### **Customizable Review Criteria**

Tailor the review process to your team's standards:

```python
PROMPT_INSTRUCTIONS = """
You are an expert software reviewer. Please review the given code diff in a pull request.
Give constructive, actionable comments on:
- Logic issues
- Suggestions for better implementation
- Time and space complexity

Only comment on what's in the diff.

If no major issues are found, leave a creative one-word compliment to make the author smile.

Checklist:
- Did Author mention Time Complexity?
- Did Author mention Space Complexity?
- Did Author explain the approach with comments?
"""
```

### **Developer Happiness**

Because great tools should make developers smile:

- ✅ **Positive Reinforcement**: Celebrates clean, well-written code
- 🎯 **Focused Feedback**: Comments only on relevant changes
- 🚀 **Learning Opportunities**: Suggests improvements that teach better practices
- 🎨 **Creative Touch**: Adds personality to the review process

## 🧪 Testing & Quality Assurance

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test modules
pytest tests/unit/test_claude.py
pytest tests/unit/test_github_utils.py
pytest tests/integration
```

## 📚 Project Structure

```
automated-pr-review/
├── 📄 main.py              # FastAPI application & webhook handler
├── 🧠 claude.py            # Claude API integration
├── 🐙 github_utils.py      # GitHub API utilities
├── 📋 models.py            # Pydantic data models
├── 📦 requirements.txt     # Python dependencies
├── 🐳 Docker               # Containerization setup
├── 🧪 tests/              # Comprehensive test suite
│   └── unit/              # Unit tests
├── 📜 scripts/            # Utility scripts
│   ├── pr_open.py         # PR creation helper
│   └── pr_close.py        # PR management helper
└── 📖 README.md           # You are here!
```
