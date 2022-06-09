const ValorantAPI = require("unofficial-valorant-api")

async function getMMR(version, region, name, tag) {
    const mmr = await ValorantAPI.getMMR(version, region, name, tag)
    //Do something with the data, for an example send it as a Discord Embed into your Discord
}

getMMR("v1", "eu", "Henrik3", "EUW3") 