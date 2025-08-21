import requests

def get_player_stats(match_id: str, player_name: str, player_tag: str):
    url = f"https://api.henrikdev.xyz/valorant/v2/match/{match_id}"
    response = requests.get(
        url,
        headers={"Authorization":"HDEV-e2fba1d7-ddec-4d6c-a41c-4b318382c3fa","Accept":"*/*"},
    )

    data = response.json()

    # 402d7dc5-aa22-4444-9f95-2652e3e2fdf8
    #player_name = "Chy"
    #player_tag = "00000"
    player_index = 0
    for player in data["data"]["players"]["all_players"]:
        if player["name"] == player_name and player["tag"] == player_tag:
            player_index = data["data"]["players"]["all_players"].index(player)
            break
    player_data = data["data"]["players"]["all_players"][player_index]

    # TODO:
    # need to manually add the  Plants, placement, defuses, first_bloods, first_death fields as they are derived from match data

    export_data = {
        "econ_rating": player_data["damage_made"] / player_data["economy"]["spent"]["overall"] * 1000,
        "headshot_percentage": (player_data["stats"]["headshots"] / (player_data["stats"]["legshots"] + player_data["stats"]["headshots"] + player_data["stats"]["bodyshots"])*100),
        "headshots": player_data["stats"]["headshots"],
        "damage": player_data["damage_made"],
        "damage_received": player_data["damage_received"],
        "ability_1_casts": player_data["ability_casts"]["c_cast"],
        "ability_2_casts": player_data["ability_casts"]["q_cast"],
        "ultimate_casts": player_data["ability_casts"]["x_cast"],
        "kills": player_data["stats"]["kills"],
        "grenade_casts": player_data["ability_casts"]["e_cast"],
        "deaths": player_data["stats"]["deaths"],
        "assists": player_data["stats"]["assists"]
        }
    return export_data