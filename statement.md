 📄 `statement.md` (Section 5.2)

```markdown
Project Statement

1. Problem Statement

The objective of this project is to build a basic, but robust, command-line implementation of the Rock-Paper-Scissors game. The project serves as a comprehensive assignment to apply and demonstrate fundamental Python programming principles, specifically focusing on **modular design,** effective **control flow structures** (if/else), and **reliable user input validation** as outlined in the course syllabus.

 2. Scope of the Project

The scope is limited to a single-user, session-based application.

* **In-Scope:** Core game logic, input/output interface, session-based score tracking, and comprehensive input validation.
* **Out-of-Scope:** Complex AI or machine learning models for opponent prediction, database integration, or a graphical user interface (GUI).

3. Target Users

The primary target users are:

* **The Player:** Any user who wants to play a simple, engaging game of Rock-Paper-Scissors via the command line.
* **The Evaluator/Instructor:** For assessment of foundational Python programming and modular design skills.

 4. High-Level Features and Functional Requirements (FR)

The system is structured into three major functional modules:

1.  **Input/Output Interface Module (FR1):** Manages user interaction, including prompting for moves, input validation, and displaying game results.
2.  **Game Logic Module (FR2):** Encapsulates the core rules (if/else statements) to accurately compare the player's and computer's moves and determine the round's outcome (Win, Loss, or Tie).
3.  **Score Tracking Module (FR3):** Maintains a dictionary-based record of the session scores for both the player and the computer, updating and displaying them after each round.

5. Non-Functional Requirements (NFR)

The following non-functional attributes have been specified:

| Requirement | Description |
| :--- | :--- |
| **NFR1: Usability** | The interface is clear, text-based, and requires minimal cognitive load, adhering to basic CLI best practices for prompts and output. |
| **NFR2: Error Handling** | The system must implement robust input validation to catch non-'r', 'p', or 's' inputs without crashing and reprompt the user. |
