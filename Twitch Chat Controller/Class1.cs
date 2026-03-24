using BepInEx;
using HarmonyLib;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;
using TwitchLib.Client;
using TwitchLib.Client.Models;
using TwitchLib.Communication.Clients;
using TwitchLib.Communication.Models;
using ManagementScripts;
using SimulationScripts.BibiteScripts;
using ScriptHelpers;

namespace Twitch_Chat_Controller
{
    [BepInPlugin(pluginGuid, pluginName, pluginVersion)]
    public class Main : BaseUnityPlugin
    {
        public const string pluginGuid = "MeltingDiamond.Twitch_Controller";
        public const string pluginName = "Twitch Chat Controller";
        public const string pluginVersion = "0.2.8";

        private Harmony harmony;

        TwitchClient client;

        public void Awake()
        {
            harmony = new Harmony(pluginGuid);
            harmony.PatchAll();
        }

        public void Start()
        {
            try
            {
                ConnectToTwitch();
                Logger.LogInfo("Twitch connection attempt started.");
            }
            catch (Exception ex)
            {
                Logger.LogError($"Failed to connect to Twitch: {ex.Message}");
            }
        }

        private void ConnectToTwitch()
        {
            string twitchUsername = "The_Bibites_Bot";  // Replace with your Twitch username
            string oauthToken = "oauth:vmj4004agxr4zby0idvhr3axvl6f7m"; // Get from https://twitchapps.com/tmi/
            string channelName = "Melting__Diamond"; // Replace with your channel name

            ConnectionCredentials credentials = new ConnectionCredentials(twitchUsername, oauthToken);
            var clientOptions = new ClientOptions
            {
                MessagesAllowedInPeriod = 750,
                ThrottlingPeriod = TimeSpan.FromSeconds(30)
            };

            WebSocketClient customClient = new WebSocketClient(clientOptions);
            client = new TwitchClient(customClient);
            client.Initialize(credentials, channelName);  // Fixed this line

            // Event Handlers
            client.OnConnected += Client_OnConnected;
            client.OnJoinedChannel += Client_OnJoinedChannel;
            client.OnMessageReceived += Client_OnMessageReceived;
            //client.OnNewSubscriber += Client_OnNewSubscriber;

            client.Connect();
        }

        private void Client_OnConnected(object sender, TwitchLib.Client.Events.OnConnectedArgs e)
        {
            Debug.Log($"Connected to Twitch as {client.TwitchUsername}");
        }

        private void Client_OnJoinedChannel(object sender, TwitchLib.Client.Events.OnJoinedChannelArgs e)
        {
            Debug.Log($"Joined channel: {e.Channel}");
            client.SendMessage(e.Channel, "The Bibites Twitch bot connected!"); //You can now control The Bibites using commands (!help)");
        }

        // Event when a viewer sends a message
        private void Client_OnMessageReceived(object sender, TwitchLib.Client.Events.OnMessageReceivedArgs e)
        {
            string message = e.ChatMessage.Message;
            string username = e.ChatMessage.Username;

            Logger.LogInfo($"Message from {username}: {message}");

            if (message.StartsWith("!"))
            {
                HandleCommand(username, message);
            }
        }

        // Command Handler
        private void HandleCommand(string username, string message)
        {
            string command = message.Split(' ')[0].ToLower(); // Get command without parameters

            switch (command)
            {
                case "!help":
                    client.SendMessage("Melting__Diamond", "Commands\n!random");
                    break;
                
                //case "!menu":
                //    ToggleMainUI();
                //    break;

                //case "!pause":
                //    TogglePause();
                //    break;

                //case "!quicksave":
                //    QuickSaveGame();
                //    break;

                case "!random":
                    SelectRandomBibite();
                    client.SendMessage("Melting__Diamond", $"{username} selected random bibite");
                    break;

                //case "!oldest":
                //    SelectOldestBibite();
                //    break;

                //case "!highgen":
                //    SelectHighGenBibite();
                //    break;

                //case "!egg":
                //    SelectRandomEgg();
                //    break;

                //case "!layegg":
                //    LayEgg();
                //    break;

                //case "!kill":
                //    KillTarget();
                //    break;

                default:
                    client.SendMessage("Melting__Diamond", $"Unknown command, {username}. Try !help");
                    break;
            }
        }

        private static readonly object lockObj = new object();

        private void SelectRandomBibite()
        {
            WorldObjectsSpawner worldObjectsSpawner = WorldObjectsSpawner.Instance;
            client.SendMessage("Melting__Diamond", $"Random bibite: {(from g in worldObjectsSpawner.allBibites where !g.GetComponent<BibiteBody>().dying select g).RandomElement<GameObject>()}");

            UserControl userControl = UserControl.Instance;
            //userControl.SelectTarget((from g in worldObjectsSpawner.allBibites
              //                 where !g.GetComponent<BibiteBody>().dying
                //               select g).RandomElement<GameObject>());

            //userControl.toRepeatOnDeath = new Action(SelectRandomBibite);
        }

        public void OnDestroy()
        {
            client?.Disconnect();
            harmony?.UnpatchSelf();
        }
    }
}
