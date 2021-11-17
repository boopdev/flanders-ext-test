from disnake.ext import commands
from .testChildDir import helperFuncs

class ExampleRepoCog(commands.Cog):
    def __init__(self, client *args, **kwargs):
        self.client

    @commands.slash_command(name="sum", description="Gets the sum of each individual number", options=[Option("numbers"),])
    async def getSumOfNumbers(self, interaction, numbers : str):
        
        if not numbers.isdigit():
            return await interaction.send("Command only accepts digit characters.") 
        
        wackySum = helperFuncs.getSum(
            list(
                map(
                    int, list(numbers)
                )
            )
        )

        return await interaction.send(
            f"**Sum of numbers:** {wackySum}"
        )


