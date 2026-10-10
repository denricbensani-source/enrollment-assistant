# Project Reflection — Bayanihan College Enrollment Helpdesk Assistant

## 1. How could incorrect AI answers affect students?

Incorrect answers could cause students to miss enrollment deadlines, submit incomplete requirements or misunderstand payment procedures. These problems could delay their enrollment or create unnecessary expenses. To reduce this risk, the chatbot uses a predefined FAQ knowledge base and is instructed not to invent college policies, dates, fees or requirements. Students should still confirm important information with the appropriate college office.

## 2. How does the system protect student privacy?

The chatbot is designed to answer general enrollment questions rather than collect sensitive personal information. Feedback records store the rating, predicted intent and related FAQ IDs instead of the complete chat message. The application also uses an environment variable for the Gemini API key so that the key does not need to be written directly into the source code. Additional privacy testing and security controls are still necessary before real-world deployment.

## 3. Could the chatbot be unfair to some students?

Yes. The chatbot may perform better for English questions than for Filipino or Taglish questions because its FAQ dataset and intent-classification training data are limited. This could make it harder for some students to get relevant answers. Testing with more questions in different languages and improving the FAQ retrieval process can help make the system more inclusive.

## 4. What happens when the chatbot does not know an answer?

The chatbot should acknowledge that the information is unavailable in its FAQ knowledge base rather than invent an answer. It should direct the student to the appropriate college office, such as Admissions, Finance, Scholarships or the Registrar. This is important because enrollment information can affect students' decisions and should be accurate.

## 5. What are the limitations of this project?

The intent classifier uses a small dataset of 50 sample questions, so its predictions may not generalize well to every student question. FAQ retrieval also needs more testing for Filipino and Taglish inputs. Gemini API access was restricted during development, so successful AI-generated responses and prompt-injection handling have not yet been verified. The admin dashboard also needs authentication before it can safely be exposed publicly.

## Conclusion

This project demonstrates how a chatbot can make enrollment information easier to access while using a defined FAQ knowledge base and collecting feedback. However, an AI assistant should not replace official college guidance. Improving accuracy, protecting student information, testing different languages and verifying AI safety are important steps before the system can be used by real students.
