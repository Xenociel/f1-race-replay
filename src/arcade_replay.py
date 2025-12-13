import os
import arcade
from src.interfaces.race_replay import ReplayView, MainMenuView, run_main_menu

# Kept these as "default" starting sizes, but they are no longer hard limits
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SCREEN_TITLE = "F1 Replay System"

"""
def run_arcade_replay(frames=None, track_statuses=None, example_lap=None, drivers=None, title=None,
                      playback_speed=1.0, driver_colors=None, circuit_rotation=0.0, total_laps=None, chart=False):
    # 1. CLI Mode Check (Single Run if arguments are provided)
    if frames is not None:
        window = F1RaceReplayWindow(
            frames=frames,
            track_statuses=track_statuses,
            example_lap=example_lap,
            drivers=drivers,
            playback_speed=playback_speed,
            driver_colors=driver_colors,
            title=title,
            total_laps=total_laps,
            circuit_rotation=circuit_rotation,
        )
        arcade.run()
        return  # Exit after single run

    # 2. Launcher Mode Loop (Handles Menu <-> Replay Window Cycling)
    print("Starting Launcher Mode Loop...")

    while True:
        # A. Run Main Menu and get selected data
        print("Running Main Menu...")
        # run_main_menu() blocks until the Menu Window is closed
        data = run_main_menu()

        if data is None:
            # User closed the menu window directly (X button or ESC on Menu) -> Exit App
            print("No race selected or exited. Exiting application.")
            break

        # B. Process selected data
        frames = data['frames']
        track_statuses = data['track_statuses']
        driver_colors = data['driver_colors']
        title = data['title']
        total_laps = data['total_laps']
        example_lap = data.get('example_lap')

        if example_lap is None:
            print("Error: example_lap data missing. Returning to menu.")
            continue  # Data error, restart the loop to show menu again

        drivers = driver_colors.keys()

        # C. Create and Run Replay Window
        window = F1RaceReplayWindow(
            frames=frames,
            track_statuses=track_statuses,
            example_lap=example_lap,
            drivers=drivers,
            playback_speed=playback_speed,
            driver_colors=driver_colors,
            title=title,
            total_laps=total_laps,
            circuit_rotation=circuit_rotation,
        )

        print("Launching Replay Window...")
        arcade.run()  # This blocks until the Replay Window is closed

        # D. Post-Close Handling
        # Check the flag set by the 'Exit to Menu' button or ESC key
        should_return = getattr(window, 'return_to_menu', False)

        # Explicitly delete the window object to free resources
        del window

        if should_return:
            # If flag is True, continue the loop to re-open the Main Menu
            print("Replay Window Closed. Continuing loop to Main Menu...")
            continue
        else:
            # If flag is False (closed via X button), break the loop -> App exit
            print("Replay Window Closed. Exiting application.")
            break
"""


def run_arcade_replay(frames=None, track_statuses=None, example_lap=None, drivers=None, title=None,
                      playback_speed=1.0, driver_colors=None, circuit_rotation=0.0, total_laps=None, chart=False):
    # 1. Create the single, main window for the entire application
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)

    # 2. Check for CLI Mode (Arguments provided)
    if frames is not None:
        # CLI Mode: Start directly in Replay View
        print("Running in CLI Mode. Launching Replay View...")

        # Instantiate the Replay View
        replay_view = ReplayView(
            window,  # Pass the window instance
            frames=frames,
            track_statuses=track_statuses,
            example_lap=example_lap,
            drivers=drivers,
            playback_speed=playback_speed,
            driver_colors=driver_colors,
            title=title,
            total_laps=total_laps,
            circuit_rotation=circuit_rotation,
        )
        # Set the initial view
        window.show_view(replay_view)
    else:
        # Launcher Mode: Start with Main Menu View
        print("No arguments provided. Launching Main Menu View...")

        # Start with the Main Menu View
        main_menu_view = MainMenuView(window)
        window.show_view(main_menu_view)

    # 3. Run the entire application loop ONCE.
    arcade.run()