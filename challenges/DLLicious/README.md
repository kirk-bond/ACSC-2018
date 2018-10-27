# CTF_DLLicious

You found a suspicious looking dll on your machine. Can you figure out what its doing?

## Flag

acsc18{dont you love windows}

## Category
Windows DLL structure/reverse engineering

## Hints
1. [deduct 15%] Direct them to look at dll documentation on MSDN (https://docs.microsoft.com/en-us/cpp/build/dlls-in-visual-cpp?view=vs-2017) 
2. [deduct 15%] Direct them to look at the dll export table using a tool. (dump bin, ida, dependency walker)
3. [deduct 50%] Explain what rundll does.

## Steps
1. Use a reverse engineering tool (dumpbin, objdump, ida, binary ninja) to view the export table 
2. Identify the exported function
3. Run the dll with the exported function (rundll32 acsc.dll,getting_closer)

## Resources required
Windows environment with dumpbin or dependency walker

## Answer
Run the dll with the exported function (rundll32 acsc.dll,getting_closer)
