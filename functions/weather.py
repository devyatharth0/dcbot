import discord
from discord.ext import commands
import requests
from config import WEATHER_API_KEY

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="weather")
    async def weather(self, ctx, city: str = None):
        if not city:
            await ctx.send("❌ Please provide a city name! Example: `!weather London`")
            return
        
        try:
            city = city.strip()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_desc = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]
                await ctx.send(
                    f"🌤️ **Weather in {city.capitalize()}**\n"
                    f"- Description: {weather_desc}\n"
                    f"- Temperature: {temp}°C\n"
                    f"- Feels Like: {feels_like}°C\n"
                    f"- Humidity: {humidity}%\n"
                    f"- Wind Speed: {wind_speed} m/s"
                )
            else:
                await ctx.send(f"❌ City not found or API error.\nDetails: {data.get('message', 'No details available.')}")
        except Exception as e:
            await ctx.send("❌ Failed to fetch weather. Try again later!")
            print(f"Weather Error: {e}")
            print(f"API Response: {data}")

async def setup(bot):
    await bot.add_cog(Weather(bot))
