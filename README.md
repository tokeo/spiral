<h1 align="center">Spiral</h1>

<p align="center">
  <strong>Spiral is the Tokeo example app!</strong>
</p>
<p align="center">
  Created with 💪 by Tom Freudenberg
</p>

<br/>

## 🚀 Welcome to Your New Journey

Congratulations on creating your **Spiral** project! This is more than just code – it's the foundation for bringing your ideas to life. Whether you're building a data analysis tool, a web service, or an AI-powered application, you've taken the first step toward creating something meaningful.

> "The best way to predict the future is to invent it." – Alan Kay

### 🎯 What's Next?

Your application is ready for you to explore and expand. Here are some exciting directions you might take:

- **AI Integration**: Add intelligence with machine learning using scikit-learn, PyTorch, or integrate with LLMs
- **Data Exploration**: Uncover insights by analyzing data with pandas, matplotlib, or seaborn
- **Web Interfaces**: Create beautiful dashboard and web tools with the built-in NiceGUI extension and tailwindcss based admin theme
- **Automation**: Schedule tasks and create workflows with the scheduler extension or total local and remote automation
- **API Development**: Build robust APIs for your services

Remember, every great application started exactly where you are now!

<br/>

## 🛠️ Getting Started

### Installation

First, set up your virtual environment:

```bash
# Create and activate virtual environment
make venv
source .venv/bin/activate

# Install development dependencies
make dev
```

### Running Your Application

Once installed, you can launch your application:

```bash
# See available commands
spiral --help

# Run a specific command
spiral <command>
```

### Compiling Protocol Buffers

If you're using gRPC services, you have to run:

```bash
# Generate Python code from proto files
make proto
```

<br/>

## 📊 Exploring Tokeo Features

### Process Background Tasks with Dramatiq (needs a running RabbitMQ)

```bash
# Launch Dramatiq workers to process background tasks
spiral dramatiq serve

# Trigger a task (e.g., count-words)
spiral emit count-words --url https://github.com
```

### Expose Services via gRPC

```bash
# Start the gRPC server for external task access
spiral grpc serve

# Execute a task using the gRPC client
spiral grpc-client count-words --url https://github.com
```

### Schedule Recurring Tasks

```bash
# Run the scheduler with interactive shell
spiral scheduler launch

# Within the scheduler shell, list and manage tasks
Scheduler> list
Scheduler> tasks pause 1 2 3  # Pause task with ID 1, 2, 3
Scheduler> tasks resume 1  # Resume task with ID 1
Scheduler> tasks fire 1  # Resume task with ID 1
```

### Automate Operations

```bash
# Run automation tasks locally or remotely
spiral automate run uname --verbose --as-json
```

### Create Web Interfaces

```bash
# Start the web interface
spiral nicegui serve

# Access the interface at http://localhost:4123
```

### Use Diskcache

```bash
# List content
spiral cache list

# Set value
spiral cache set counter --value 1 --value-type int

# Get value
spiral cache get counter
```

<br/>

## 📊 Development Tools

This project includes several helpful commands to streamline your development:

```bash
# Format your code
make fmt

# Run linting checks
make lint

# Run tests
make test

# Run tests with coverage report
make test cov=1

# Build documentation
make doc

# Check for outdated dependencies
make outdated
```

<br/>

## 🚀 Deployment Options

### Package Your Application

```bash
# Create source distribution
make sdist

# Create wheel package
make wheel

# Build Docker image
make docker
```

<br/>

## Control Logging

Set log levels via config, environment variables, or CLI flags:

```bash
# App debug logs
SPIRAL_LOG_COLORLOG_LEVEL=debug spiral command

# App + framework debug logs
spiral --debug command

# Framework debug logs only
CEMENT_LOG=1 spiral command
```

<br/>

## 📚 Project Structure

Your project is organized into a clean, modular structure:

- `config/` - Configuration files for prod, stage, dev and test environments
- `spiral/controllers/` - Command-line interface controllers
- `spiral/core/logic` - Space for your core application logic
- `spiral/core/grpc/` - gRPC service definitions and implementations
- `spiral/core/pages/` - Web interface pages and apis
- `spiral/core/tasks/` - Implementations of actors, agents, automations, operations, performers etc.
- `spiral/core/utils/` - A place to put your overall tools and helper functions
- `spiral/templates/` - Templates for rendering content
- `tests/` - Test suite to ensure reliability

<br/>

## 🌟 Making It Your Own

This is just the beginning of your journey. As you build and shape this project, consider:

- What problem are you trying to solve?
- Who will use your application and how?
- How can you make it not just functional, but delightful to use?

<br/>

## 🔄 Continuous Improvement

Keep your project healthy with these practices:

- Document your code and add examples
- Write tests for new features
- Refactor when needed for clarity
- Stay up-to-date with your packages using `make outdated`

<br/>

## 🤝 Need Help?

If you encounter challenges or have questions:

- Check the Tokeo documentation
- Explore similar open-source projects for inspiration
- Connect with the community of developers

<br/>
<br/>

<p>
  Built with ❤️ and <a href="https://github.com/tokeo/tokeo">tokeo</a> - Empowering Python Applications
</p>
