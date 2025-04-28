FROM mcr.microsoft.com/dotnet/sdk AS build
WORKDIR /source
COPY *.csproj .
RUN dotnet restore

COPY . .
RUN dotnet publish -c Release -o /app 

# app image
FROM mcr.microsoft.com/dotnet/runtime
WORKDIR /app
COPY --from=build /app .
ENTRYPOINT ["dotnet", "Worker.dll"]