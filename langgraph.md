# Intro
`LangGraph` is a framework that allows you to build production-ready applications by giving you control tools over the flow of your agent.

`LangGraph` and  `LangChain` are different and can be used in isolation, but, in the end, all resources you will find online use both packages hand in hand.

Use LangGraph when you need control and predictability in your AI application.

- LLM systems balance freedom vs control
    - Free agents (like code agents) are flexible and creative but harder to predict
    - Controlled systems are more reliable and easier to guard

- LangGraph focuses on control
    - Lets you define clear steps, decision points, and execution flow
    - Ensures the agent follows a predictable process

- It’s ideal when:
    - Tasks must happen in a specific order
    - Different decisions are made at different steps
    - You need reliability over creativity

**In short:** use `LangGraph` when your agent must follow a structured, rule-based workflow rather than act freely.


# How LangGraph works (in plain terms):

LangGraph lets you design your AI app like a flowchart.

**Nodes** = individual steps(python functions)
Each node does one thing (call an LLM, run a tool, check a condition, etc.).

**Edges** = paths between steps
They decide what happens next after a node finishes.

**State** = shared memory
This is information you define (inputs, intermediate results, decisions).
Every node can read and update this state.

How it runs:
- A node executes
- It updates the state
- Based on the current state, LangGraph chooses the next node via the edges
- This repeats until the flow ends

**How is it different from regular python? Why do I need LangGraph?**
It includes states, visualization, logging (traces), built-in human-in-the-loop, and more.

## Building Blocks of LangGraph
An application in LangGraph starts from an entrypoint, and depending on the execution, the flow may go to one function or another until it reaches the END.