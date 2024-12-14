# Film Shoot Planner Chatbot
Too many things going on in your head while planning a film shoot internationally? Worry not! This chatbot is the best partner to help you plan all international shoots. This chatbot, built using Langgraph handles different needs of the user with it's statefulness

## Tech Stack
- **[Langgraph]([url](https://www.langchain.com/langgraph))**: a framework to build a chatbot with graph-like architecture
- **Flask**: to create a server that retrieves data from the database
- **PostgreSQL**: to store stuctured crew data

## Architecture
![architecture](https://github.com/user-attachments/assets/df317d02-903f-4531-b0f6-74b31e11aed4)

## Nodes and their functions
1. **Crew**: Handles queries related to the crew of the user
2. **Equipment**: Gives information about the film rental equipments
3. **Culture**: Gives details about the culture of destination country
4. **Logistics**: Takes care about the travel and accomodation in the destination country
5. **Compliance**: Looks after the protocols to be kept in mind while preparing for a shoots abroad

## Flask Server
1. crew_desc : This function extracts description of user's crew from PostgreSQL database
2. location : This extracts only location of user from PostgreSQL database

## Output 
The output received while prompting for a film shoot in Japan is given in a text file: [File](japan-bot-output.txt) 
