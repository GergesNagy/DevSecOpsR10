# Use the official .NET SDK image for building
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build

# Set working directory
WORKDIR /src

# Copy the project file and restore dependencies
COPY Worker.csproj ./
RUN dotnet restore

# Copy the rest of the code and build
COPY . ./
RUN dotnet publish -c Release -o /app/publish

# Use a runtime image for final output
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final

# Set working directory
WORKDIR /app

# Copy the published output
COPY --from=build /app/publish .

# Entry point
ENTRYPOINT ["dotnet", "Worker.dll"]
