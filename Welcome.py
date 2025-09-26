#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Skull ASCII Art Display
Fokus pada tampilan visual yang keren
"""

import os
import time


class SkullDisplay:
    def __init__(self):
        # Colors
        self.RED = "\033[91m"
        self.GREEN = "\033[92m"
        self.BLACK = "\033[90m"
        self.WHITE = "\033[97m"
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"

    def clear_screen(self):
        os.system("clear" if os.name == "posix" else "cls")

    def skull_banner(self):
        """Banner utama dengan tengkorak besar dan Welcome Tuan"""
        skull = f"""
{self.RED}                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{self.RED}                              ░░░░░░░░░░░░░░{self.BLACK}████████{self.RED}░░░░░░░░░░░░░░░░░
{self.RED}                              ░░░░░░░░░░{self.BLACK}████████████{self.RED}░░░░░░░░░░░░░░
{self.RED}                              ░░░░░░░░{self.BLACK}████████████████{self.RED}░░░░░░░░░░░
{self.RED}                              ░░░░░░{self.BLACK}██{self.WHITE}██{self.BLACK}████████{self.WHITE}██{self.BLACK}██{self.RED}░░░░░░░░░
{self.RED}                              ░░░░░{self.BLACK}███{self.WHITE}███{self.BLACK}██████{self.WHITE}███{self.BLACK}███{self.RED}░░░░░░░
{self.RED}                              ░░░░{self.BLACK}████{self.WHITE}███{self.BLACK}██████{self.WHITE}███{self.BLACK}████{self.RED}░░░░░
{self.RED}                              ░░░{self.BLACK}█████{self.WHITE}██{self.BLACK}████████{self.WHITE}██{self.BLACK}█████{self.RED}░░░
{self.RED}                              ░░{self.BLACK}██████████████████████{self.RED}░░
{self.RED}                              ░{self.BLACK}████████████████████████{self.RED}░
{self.RED}                              {self.BLACK}█████████{self.WHITE}██{self.BLACK}████{self.WHITE}██{self.BLACK}█████████
{self.RED}                              {self.BLACK}██████████{self.WHITE}████{self.BLACK}██████████
{self.RED}                              {self.BLACK}███████████{self.WHITE}██{self.BLACK}███████████
{self.RED}                              {self.BLACK}████████████████████████     {self.GREEN}██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
{self.RED}                              {self.BLACK}█████{self.WHITE}██████████████{self.BLACK}█████     {self.GREEN}██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
{self.RED}                              {self.BLACK}████{self.WHITE}████████████████{self.BLACK}████     {self.GREEN}██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
{self.RED}                              {self.BLACK}███{self.WHITE}██████████████████{self.BLACK}███     {self.GREEN}██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
{self.RED}                              {self.BLACK}██{self.WHITE}████████████████████{self.BLACK}██     {self.GREEN}╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
{self.RED}                              {self.BLACK}█{self.WHITE}██████████████████████{self.BLACK}█     {self.GREEN} ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
{self.RED}                              {self.WHITE}████████████████████████
{self.RED}                              {self.WHITE}████████████████████████          {self.RED}████████╗██╗   ██╗ █████╗ ███╗   ██╗
{self.RED}                              ░{self.WHITE}██████████████████████{self.RED}░          {self.RED}╚══██╔══╝██║   ██║██╔══██╗████╗  ██║
{self.RED}                              ░░{self.WHITE}████████████████████{self.RED}░░             {self.RED}██║   ██║   ██║███████║██╔██╗ ██║
{self.RED}                              ░░░{self.WHITE}██████████████████{self.RED}░░░             {self.RED}██║   ██║   ██║██╔══██║██║╚██╗██║
{self.RED}                              ░░░░{self.WHITE}████████████████{self.RED}░░░░             {self.RED}██║   ╚██████╔╝██║  ██║██║ ╚████║
{self.RED}                              ░░░░░{self.WHITE}██████████████{self.RED}░░░░░             {self.RED}╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
{self.RED}                              ░░░░░░{self.WHITE}████████████{self.RED}░░░░░░
{self.RED}                              ░░░░░░░{self.WHITE}██████████{self.RED}░░░░░░░                    {self.BLACK}💀 SKULL HACKER TOOLS 💀
{self.RED}                              ░░░░░░░░{self.WHITE}████████{self.RED}░░░░░░░░                    {self.WHITE}Educational Display Only
{self.RED}                              ░░░░░░░░░{self.WHITE}██████{self.RED}░░░░░░░░░                    {self.GREEN}━━━━━━━━━━━━━━━━━━━━━━
{self.RED}                              ░░░░░░░░░░{self.WHITE}████{self.RED}░░░░░░░░░░
{self.RED}                              ░░░░░░░░░░░{self.WHITE}██{self.RED}░░░░░░░░░░░
{self.RED}                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{self.RESET}
        """
        return skull

    def menu_display(self):
        """Menu sebagai pajangan visual saja"""
        menu = f"""
{self.BLACK}         ╔════════════════════════════════════════════╗
{self.BLACK}         ║  {self.RED}💀           SKULL MENU           💀{self.BLACK}  ║
{self.BLACK}         ╠════════════════════════════════════════════╣
{self.GREEN}         ║  {self.WHITE}[1] ☠️  ASCII Art Generator            {self.BLACK}║
{self.GREEN}         ║  {self.WHITE}[2] 🦴  Network Scanner               {self.BLACK}║
{self.GREEN}         ║  {self.WHITE}[3] ⚰️   Web Scraper                  {self.BLACK}║
{self.GREEN}         ║  {self.WHITE}[4] 🔪  Port Scanner                  {self.BLACK}║
{self.GREEN}         ║  {self.WHITE}[5] ⚔️   IP Tracker                   {self.BLACK}║
{self.GREEN}         ║  {self.WHITE}[6] 💀  Brute Force                  {self.BLACK}║
{self.GREEN}         ║  {self.WHITE}[7] 🏴‍☠️  Advanced Tools               {self.BLACK}║
{self.GREEN}         ║  {self.WHITE}[8] 👑  Elite Hacker Mode            {self.BLACK}║
{self.BLACK}         ╚════════════════════════════════════════════╝
{self.RED}                    💀 DISPLAY ONLY - NO FUNCTIONS 💀{self.RESET}
        """
        return menu

    def footer_display(self):
        """Footer dengan info tambahan"""
        footer = f"""
{self.GREEN}    ┌─────────────────────────────────────────────────────────────┐
{self.GREEN}    │  {self.RED}⚠️  WARNING: EDUCATIONAL DISPLAY ONLY  ⚠️{self.GREEN}            │
{self.GREEN}    │  {self.WHITE}This is just a visual demonstration tool            {self.GREEN}│
{self.GREEN}    │  {self.WHITE}No actual hacking functions are implemented        {self.GREEN}│
{self.GREEN}    │  {self.BLACK}Created for learning ASCII art and terminal styling{self.GREEN} │
{self.GREEN}    └─────────────────────────────────────────────────────────────┘{self.RESET}
        """
        return footer

    def animated_dots(self):
        """Animasi loading dots"""
        for i in range(3):
            for dots in ["", ".", "..", "..."]:
                print(
                    f"\r{self.GREEN}💀 Loading Skull Tools{dots}    {self.RESET}",
                    end="",
                )
                time.sleep(0.3)


def main():
    skull = SkullDisplay()

    # Clear screen
    skull.clear_screen()

    # Tampilkan loading animation
    skull.animated_dots()
    print()

    # Clear dan tampilkan banner utama
    skull.clear_screen()
    print(skull.skull_banner())

    # Tampilkan menu pajangan
    print(skull.menu_display())

    # Tampilkan footer
    print(skull.footer_display())

    # Loop untuk menjaga tampilan
    while True:
        try:
            user_input = input(
                f"\n{skull.RED}💀 Press Enter to refresh display or 'q' to quit: {skull.RESET}"
            )
            if user_input.lower() == "q":
                print(
                    f"{skull.GREEN}☠️ Thanks for viewing Skull Display, Tuan! ☠️{skull.RESET}"
                )
                break
            else:
                # Refresh display
                skull.clear_screen()
                print(skull.skull_banner())
                print(skull.menu_display())
                print(skull.footer_display())

        except KeyboardInterrupt:
            print(f"\n{skull.RED}💀 Skull Display terminated 💀{skull.RESET}")
            break


if __name__ == "__main__":
    main()
