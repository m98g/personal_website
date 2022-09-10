# Personal Website:
The code for my personal website. The images and downloads used were removed but this template can be adapted to other usecases.
If you are looking for an easy way to make a website I can recommend you fastapi as the backend and tailwindcss for the frontend.
The stack is minimalistic but works great for a simple portfolio website.

## Start local server
To start a local server with this code simply run:

`uvicorn main:app --reload`

The reload flag is so that the server watches your files for changes.

## Start tailwind build process
You need to have tailwind css installed on your machine. For this follow their guide: https://tailwindcss.com/docs/installation.
They assume that you have node.js installed on your machine.

To start the build process of tailwind run this command from within the tailwindcss directory:

`npx tailwindcss -i ./styles/app.css -o ../static/css/app.css --watch`

The watch flag is again so that the build process is completed each time you enter changes into the tracked html files.

Not all files are tracked by the config file, because in the complete code I have some html that I did not want to track.
If you want to track all of the html files simply replace the indside of the content with *.html.

## Deployment

Pick your poison. I deployed the fastapi app using azures services because I am a student and they have an excellent student account services.
