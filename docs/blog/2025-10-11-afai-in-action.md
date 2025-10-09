
---
layout: post
title:  "AFAI in Action: A Practical Guide to the Demo"
date:   2025-10-11 13:00:00 -0500
categories: afai
---

The Agency First AI (AFAI) framework is more than just a theoretical concept. It's a practical tool for building more responsible and ethical AI systems. To help you understand how AFAI works in practice, we've created a demo harness that simulates an AI-human interaction and calculates the Agency Preservation Score (APS) in real-time.

In this post, we'll walk you through the process of running the demo and interpreting its output. Before you begin, make sure you have Python installed on your system.

First, clone the AFAI repository from GitHub:

```bash
git clone https://github.com/AgencyFirstAI/afai-manifesto.git
```

Next, navigate to the `demo` directory and run the `run_demo.py` script:

```bash
cd afai-manifesto/demo
python run_demo.py
```

The script will simulate a scenario in which an AI agent is assisting a user with a task. As the simulation runs, you'll see the APS being calculated and displayed in the console. The output will show you how the APS changes in response to different types of AI behavior.

By experimenting with the demo, you can gain a deeper understanding of the AFAI framework and the importance of agency preservation. We encourage you to explore the code, modify the simulation parameters, and see for yourself how different AI design choices can impact human agency.

In our next post, we'll dive deeper into the `afai_lib` library and show you how you can use it to integrate AFAI into your own projects.
