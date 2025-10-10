# Project TODO List

This list summarizes the suggestions for improving the AFAI Manifesto project.

## Bug Fixes
- [ ] **Navbar in Sub Menus is broken:**
    - [ ] Navigation gives a 404 warning if inside a blog or other sub page. 

## Front-End & Website

- [ ] **Adopt a Static Site Generator:**
    - [ ] Choose a static site generator (e.g., Jekyll, Hugo).
    - [ ] Convert the existing site structure to use templates and layouts.
    - [ ] Automate the conversion of markdown files to HTML.

- [ ] **Implement the Live Demo:**
    - [ ] Option 1: Use Pyodide to run the Python demo script in the browser.
    - [ ] Option 2: Create a simple backend API (Flask or FastAPI) to serve the demo results.

## Back-End & Python

- [ ] **Add Unit Tests:**
    - [ ] Write unit tests for the `afai_lib` library, especially the `calculate_aps` function.
    - [ ] Use `unittest` or `pytest` for the testing framework.

- [ ] **Improve Code Documentation:**
    - [ ] Add comments and docstrings to the Python code in `afai_lib`.

## Project Structure & Tooling

- [ ] **Update Version Control:**
    - [ ] Add the generated HTML directory to `.gitignore`.
    - [ ] Only commit the source markdown and template files.

- [ ] **Enhance the README:**
    - [ ] Add a more detailed project description.
    - [ ] Include setup and development instructions.
    - [ ] Provide guidelines for contributors.

---

## Marketing & Philosophy

- [ ] **Flesh out Philosophical Underpinnings:**
    - [ ] Explicitly connect the AFAI Manifesto to established philosophical concepts (e.g., Kant, existentialism).

- [ ] **Refine Liam's Persona & Communication:**
    - [ ] Develop a more nuanced communication strategy for Liam to avoid being perceived as overly rigid.
    - [ ] Create more collaborative and less confrontational simulation scenarios.

- [ ] **Improve Branding and Messaging:**
    - [ ] Brainstorm a more user-friendly name for the "Agency Preservation Score" for public communication.
    - [ ] Develop targeted messaging and content for different audiences (developers, policymakers, general public).

- [ ] **Strengthen Call to Action:**
    - [ ] Add more engaging calls to action, such as "Join the community" or "Contribute on GitHub."

- [ ] **Expand Content Strategy:**
    - [ ] Write case studies of existing AI systems.
    - [ ] Conduct interviews with experts in AI ethics, philosophy, and law.
    - [ ] Create shareable videos or infographics to explain AFAI concepts.

## Ease of Use

- [ ] **Create a text-to-speech button:**
    - [ ] Integrate Toolbelt.Blazor.SpeechSynthesis into the project
    - [ ] Add speech buttons to each blog and discussion
- [ ] **Add highlight tracking:**
    - [ ] add onboundry properties to the text and slowly scroll the highlight while listening

## Consumption Road Map

- [ ] **Land page should lead into a guided tour:**
    - [ ] Create a plan for guiding and listening
    - [ ] Suggest turning on the TTS and defaulting all additional pages to automatically use it on load
    - [ ] As each reading ends, auto navigate to the next page in the guided tour.
    - [ ] Visualize the road map in the nav bar and have it progress as the tour continues. 
    - [ ] "Continue tour later" button. 