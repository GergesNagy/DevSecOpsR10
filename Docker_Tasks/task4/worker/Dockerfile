FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build       

WORKDIR /source

COPY *.csproj .

RUN dotnet restore

COPY . .

RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/runtime:7.0 AS runtime

WORKDIR /app

COPY --from=build /source/out .

ENTRYPOINT ["dotnet", "Worker.dll"]

