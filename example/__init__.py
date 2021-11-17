from . import exampleCog

def setup(client):
    client.add_cog(exampleCog.ExampleRepoCog(client))