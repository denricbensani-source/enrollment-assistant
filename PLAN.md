# Enrollment Helpdesk Assistant — Project Plan

## Project Goal
Build an AI-powered enrollment helpdesk assistant for Bayanihan College using Flask, Python, scikit-learn and the Gemini API.

## User Stories
- [x] As a student, I want to ask enrollment questions in English or Filipino.
- [x] As a student, I want to receive answers based on the enrollment FAQ.
- [x] As a student, I want to see related FAQ references.
- [x] As a student, I want to rate answers as helpful or not helpful.
- [ ] As a student, I want accurate answers without unrelated FAQ information.
- [x] As an administrator, I want to view feedback statistics.
- [ ] As an administrator, I want access to a protected admin dashboard.
- [ ] As a developer, I want the Gemini API key stored securely as an environment variable.
- [ ] As a developer, I want to deploy the application to Render.

## Development Backlog
- [x] Create the Flask application and chat interface.
- [x] Create the FAQ knowledge base with at least 15 entries.
- [x] Create the intent dataset with 50 sample questions.
- [x] Train and save the intent classification model.
- [x] Implement FAQ retrieval and fallback answers.
- [x] Add feedback collection.
- [x] Implement the statistics API.
- [x] Build the admin dashboard.
- [x] Add project dependencies and `.gitignore`.
- [ ] Improve retrieval accuracy for English, Filipino and Taglish questions.
- [ ] Test prompt injection, private-data requests and unsupported questions.
- [ ] Verify Gemini API access and AI responses.
- [ ] Add access control to the admin dashboard.
- [ ] Complete evaluation documentation.
- [ ] Write the project reflection.
- [ ] Prepare the README and deployment instructions.
- [ ] Deploy to Render and verify the deployed application.
- [ ] Record the project demonstration.

## Current Status
The Flask chatbot, FAQ retrieval, intent model, feedback collection, statistics API and admin dashboard have been implemented. Gemini API access is currently restricted, so AI-generated responses have not yet been successfully verified. Deployment and security testing remain outstanding.