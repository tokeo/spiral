<h1 align="center">Spiral</h1>

<p align="center">
  <strong>Spiral is easily crafted with Tokeo and is the example app!</strong>
</p>
<p align="center">
  Created with 💪 by Tom Freudenberg
</p>

<br/>

## 🚀 Spiral: Experience Tokeo in Action

[Spiral](https://github.com/tokeo/spiral) takes you on an interactive journey through
[Tokeo's](https://github.com/tokeo/tokeo) capabilities, providing a fully functional environment
where you can witness Event-Driven Architecture in real-time.

With the pre-configured [Spiral Docker image](https://hub.docker.com/u/tokeocli) that includes an
activated RabbitMQ server and interactive shell, you can explore working examples of task processing,
scheduling, and automation while monitoring the entire system through a multi-window interface.

Whether you're evaluating Tokeo for your next project or simply curious about modern Python backend architectures,
Spiral offers an immersive test flight that demonstrates the power and elegance of event-driven systems
without the setup overhead.

Spiral is also where Tokeo's governed AI runtime comes alive: it ships **akili**, a train-first micro
language model (378,240 parameters, ~1.5 MB) that plans calendar tool calls through the same guarded
agent pipeline as any large provider. No weights are shipped -- you train them yourself on CPU in
minutes, then ask in English or German and watch every tool call pass validate, policy, and audit.

### Run the full working Spiral example

```bash
# Just start the interactive spiral image
docker run -p 8080:8080 -p 9999:9999 -p 50051:50051 -it tokeocli/spiral

# Launch the spiral interactive example inside the shell
launch

# Open local browser to get the spiral dashboard app
# https://localhost:8080

# Open local browser to get the spiral doc app
# https://localhost:9999
```

<br/>

Kickstart your EDA projects with **tokeo** and experience a seamless development cycle.

Cheers<br/>
Tom

<br/>

## 💪 Why Choose Tokeo?

Tokeo is a robust CLI framework for task automation, message queues, and web interfaces, making it ideal for Python backend projects. Key features include:

- **Integrated EDA Stack**: Combines Dramatiq, RabbitMQ, and gRPC for efficient task processing and external access, plus APScheduler for scheduled jobs.
- **Governed AI Agents**: A provider-agnostic AI runtime (`tokeo.ext.ai`) with typed contracts, profiles, and agents as plain configuration -- every tool call passes a guard pipeline (validate, policy, audit) and leaves a full trace. Spiral ships `akili`, a trainable micro model, to prove it end to end.
- **Encrypted Secrets in Config**: The vault extension (`tokeo.ext.vault`) keeps credentials encrypted inside your YAML (`!vault:<profile>` tags, built-in `enc` and `scrypt` handlers, keys from the environment) and decrypts them transparently at the leaf -- consumer code never changes, plaintext never lands in the config.
- **Flexible Task Automation**: Use Fabric-based tools (`tokeo.ext.automate`) to define and run local or remote tasks, with flexible configuration via YAML and CLI overrides.
- **Extensible CLI**: Built on Cement, Tokeo supports custom commands and plugins, simplifying complex workflows with minimal setup.
- **Developer-Friendly Tools**: The `Makefile` provides one-liners for formatting (`fmt`), linting (`lint`), testing (`test`), and packaging (`sdist`, `wheel`), speeding up development.
- **DiskCache** by `tokeo.ext.diskcache` enhances performance with disk-based caching for frequently accessed data, reducing load times and improving efficiency.
- **Manage task execution rates** using `temper` and `throttle` to prevent overloading with rate-limiting tools, ensuring stable and controlled processing.
- **SMTP with Jinja2 Templates**: Send emails with precise, individualized content using Jinja2 templates, supporting text, HTML, inline images, and attachments for dynamic communications.
- **Simple debugging** when using `app.inspect`. Provides basic debugging tools to inspect application state of vars and objects.
- **Web Interface**: Create beautiful UIs with the built-in NiceGUI extension to visualize data and interact with your application.

Whether you're building microservices, automating workflows, or prototyping, Tokeo provides the structure and flexibility to get started quickly.

<br/>
<br/>
<br/>

## 🚀 Welcome to Your New Journey

Congratulations on creating your **Spiral** project! This is more than just code – it's the foundation for bringing your ideas to life. Whether you're building a data analysis tool, a web service, or an AI-powered application, you've taken the first step toward creating something meaningful.

> "The best way to predict the future is to invent it." – Alan Kay

### 🎯 What's Next?

Your application is ready for you to explore and expand. Here are some exciting directions you might take:

- **Agentic AI**: Built in and governed, ask via `spiral ai ask`, every tool call passes validate, policy and audit. Trained own micro model in `core/akili`.
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
# Reminder: It can be used directly when running
# via docker image from local instance shell
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

### Ask an AI Agent

Your application speaks to AI providers through one governed runtime -- **the model plans, the pipeline governs, the tools compute**. Profiles and agents are plain YAML in `config/`: `audited` records everything and forbids nothing, `guarded` adds validation and policy. The tools are your own plain functions in `spiral/core/ai/tools/`, activated in groups per profile.

```bash
# The mock provider answers without any external service
spiral ai ask "ping"

# Inspect agents, profiles, and registered tools
spiral ai list
```

Your project also ships **akili**, a train-first micro LLM (378,240 parameters, ~1.5 MB) that plans calendar tool calls. No weights are included -- you create them, and that is the point:

```bash
# Train on your machine (CPU is fine)
python -m spiral.core.akili.train

# Then ask, in English or German -- guarded, traced, deterministic
spiral ai ask "the weekday of today plus 2 days" --profile akili --agent guarded
spiral ai ask "welches datum ist übermorgen" --profile akili
```

The model's whole language lives in `spiral/core/akili/AKILI-LEX.yaml`: teach it new words and sentence patterns by editing the file and retraining. `AKILI-LLM.md` next to it explains training, the anatomy of the weights, and grammar-constrained decoding with detailed diagrams.


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
- `spiral/core/logic` - Space for your core application logic
- `spiral/core/tasks/` - Implementations of actors, agents, automations, operations, performers etc.
- `spiral/core/ai/` - Your AI providers and plain-function tools behind the guarded contracts
- `spiral/core/akili/` - The train-first micro LLM lab: model, lexicon (`AKILI-LEX.yaml`), teaching docs
- `spiral/core/grpc/` - gRPC service definitions and implementations
- `spiral/core/utils/` - A place to put your overall tools and helper functions
- `spiral/controllers/` - Command-line interface controllers
- `spiral/site/` - Web interface pages and apis
- `spiral/templates/` - Templates for rendering content
- `tests/` - Test suite to ensure reliability

<br/>

## 🌟 Making It Your Own

This is just the beginning of your journey. As you build and shape this project, consider:

- What problem are you trying to solve?
- Who will use your application and how?
- How can you make it not just functional, but delightful to use?
- Which routine work could a governed agent take over and which tools would you trust it with?

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

Built with ❤️ and <a href="https://github.com/tokeo/tokeo">tokeo</a> - Empowering Python Applications
