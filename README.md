To test this api locally with your own mongodb URI link in any studio code or command prompt:

Fork this repository and download it

Create your own mongodb atlas database and replace collection names with whatever yours are in the code!

run pip install -r requirements.txt in the same folder

If running locally you can directly put the link in the MONGO_URI variable otherwise use a environment variable!

Finally if running locally add the following line of code at the end!

if __name__=="__main__":
    uvicorn.run(app)

If one needs help hosting this api for free for a small hobby project let me know in Issues/Discussions.
