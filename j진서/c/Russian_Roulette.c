#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

BOOL executeShutdown()
{
    printf("Shutting down...\n");
    Sleep(5000);
    return ExitWindowsEx(EWX_SHUTDOWN, SHTDN_REASON_MAJOR_OTHER | SHTDN_REASON_MINOR_OTHER | SHTDN_REASON_FLAG_PLANNED);
}

void showOutputWindow(const char *output)
{
    AllocConsole();

int main()
{
    const char *dir = "C:\\Users\\Jin\\Desktop\\Test";
    srand((unsigned int)time(NULL));
    int random_number = rand() % 6 + 1; // Adjusted random range
    if (random_number == 1)
    {
        if (RemoveDirectoryA(dir))
        {
            printf("Directory deleted successfully!\n");
            if (executeShutdown())
            {
                printf("Shutdown initiated successfully.\n");
            }
            else

            {
                printf("Error initiating shutdown.\n");
            }
        } 
        else
        {
            DWORD dwError = GetLastError();
            printf("Error deleting the directory. Error code: %d\n", dwError);
        }
    }
    else
    {
        printf("Not deleting directory.\n");
    }
    showOutputWindow("Wait for your next turn\n");
    return 0;
}
