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

### Run the full working Spiral example

```bash
# Just start the interactive spiral image
docker run -p 8080:8080 -it tokeocli/spiral

# Launch the spiral interactive example inside the shell
launch

# Open local browser to get the spiral dashboard app
# https://localhost:8080
```

<br/>

Kickstart your EDA projects with **tokeo** and experience a seamless development cycle.

Cheers<br/>
Tom

<br/>

## 💪 Why Choose Tokeo?

Tokeo is a robust CLI framework for task automation, message queues, and web interfaces, making it ideal for Python backend projects. Key features include:

- **Integrated EDA Stack**: Combines Dramatiq, RabbitMQ, and gRPC for efficient task processing and external access, plus APScheduler for scheduled jobs.
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

Built with ❤️ and <a href="https://github.com/tokeo/tokeo">tokeo</a> - Empowering Python Applications
