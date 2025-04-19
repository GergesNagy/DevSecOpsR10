# Use the official .NET SDK image to build the app
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build

WORKDIR /source

# Copy csproj and restore dependencies
# Why split the copy process?
# Every time any file changes — even a comment in Program.cs — Docker sees that the whole context is "new" and re-runs dotnet restore every time. That's wasteful, because NuGet packages likely haven’t changed. So we split them.
COPY *.csproj .

RUN dotnet restore

COPY . .

RUN dotnet publish -c Release -o out

# Use a smaller runtime image to run the app
FROM mcr.microsoft.com/dotnet/runtime:7.0 AS runtime

WORKDIR /app

COPY --from=build /source/out .

# Command to run the app
ENTRYPOINT ["dotnet", "Worker.dll"]