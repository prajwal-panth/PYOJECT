#include "decoration.h"
#include <stdio.h>

const char RWHITE[] = "\x1b[0;1;37;41m";
const char Grey[] = "\033[0;30m";
const char Red[] = "\033[0;31m";
const char Green[] = "\033[0;32m";
const char Yellow[] = "\033[0;33m";
const char Blue[] = "\033[0;34m";
const char Pink[] = "\033[0;35m";
const char Cyan[] = "\033[0;36m";
const char White[] = "\033[0;37m";
const char BrightGrey[] = "\033[0;90m";
const char BrightRed[] = "\033[0;91m";
const char BrightGreen[] = "\033[0;92m";
const char BrightYellow[] = "\033[0;93m";
const char BrightBlue[] = "\033[0;94m";
const char BrightPink[] = "\033[0;95m";
const char BrightCyan[] = "\033[0;96m";
const char BrightWhite[] = "\033[0;97m";
const char Reset[] = "\033[0;0m";

void calc_ascii()
{
    printf("%s+===============================================+%s\n", Green, Reset);
    printf("%s|  ____      _            _       _             |%s\n", Green, Reset);
    printf("%s| / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ |%s\n", Green, Reset);
    printf("%s|| |   / _` | |/ __| | | | |/ _` | __/ _ \\| '__||%s\n", Green, Reset);
    printf("%s|| |__| (_| | | (__| |_| | | (_| | || (_) | |   |%s\n", Green, Reset);
    printf("%s| \\____\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|   |%s\n", Green, Reset);
    printf("%s+===============================================+%s\n", Green, Reset);
}

void color_box()
{
    const char D_GRAY[] = "\033[48;5;232m";
    const char D_RED[] = "\033[48;5;52m";
    const char D_GREEN[] = "\033[48;5;22m";
    const char D_ORANGE[] = "\033[48;5;130m";
    const char D_BLUE[] = "\033[48;5;19m";
    const char D_MAGENTA[] = "\033[48;5;53m";
    const char D_CYAN[] = "\033[48;5;25m";
    const char D_WHITE[] = "\033[48;5;255m";
    const char GRAY[] = "\033[48;5;240m";
    const char RED[] = "\033[48;5;196m";
    const char GREEN[] = "\033[48;5;46m";
    const char ORANGE[] = "\033[48;5;214m";
    const char BLUE[] = "\033[48;5;21m";
    const char MAGENTA[] = "\033[48;5;201m";
    const char CYAN[] = "\033[48;5;51m";
    const char WHITE[] = "\033[48;5;231m";
    const char RESET[] = "\033[0;0;0m"; //\033[0m and \033[0;0;0m same

    printf("%s    %s    %s    %s    %s    %s    %s    %s    %s\n",
        D_GRAY, D_RED, D_GREEN, D_ORANGE, D_BLUE, D_MAGENTA, D_CYAN, D_WHITE, RESET);

    printf("%s    %s    %s    %s    %s    %s    %s    %s    %s\n",
        GRAY, RED, GREEN, ORANGE, BLUE, MAGENTA, CYAN, WHITE, RESET);
}