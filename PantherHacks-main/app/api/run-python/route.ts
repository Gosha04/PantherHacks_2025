import { NextResponse } from "next/server";
import { spawn } from "child_process";
import path from "path";

export async function POST(request: Request) {
  try {
    const body = await request.json(); // Get request body

    const scriptPath = path.join(process.cwd(), "scripts", "upload.py"); // Ensure 'your_script.py' exists
    const pythonProcess = spawn("python3", [scriptPath]);

    // Use a Promise to handle the asynchronous Python script execution
    const scriptOutput = await new Promise<{ output?: string; error?: string }>((resolve) => {
      let output = "";
      let errorOutput = "";

      pythonProcess.stdin.write(JSON.stringify(body));
      pythonProcess.stdin.end();

      pythonProcess.stdout.on("data", (data) => {
        output += data.toString();
      });

      pythonProcess.stderr.on("data", (data) => {
        console.error("Python stderr:", data.toString());
        errorOutput += data.toString(); // Capture stderr
      });

      pythonProcess.on("close", (code) => {
        if (code !== 0) {
          console.error(`Python script exited with code ${code}`);
          resolve({ error: errorOutput || "Python script failed" });
        } else {
          resolve({ output });
        }
      });

      pythonProcess.on("error", (err) => {
        console.error("Failed to start Python process:", err);
        resolve({ error: "Failed to start Python process" });
      });
    });

    if (scriptOutput.error) {
      return NextResponse.json({ error: scriptOutput.error }, { status: 500 });
    }

    try {
      // Assuming the Python script outputs valid JSON to stdout
      const parsedOutput = JSON.parse(scriptOutput.output || "{}");
      return NextResponse.json(parsedOutput); // Use NextResponse for App Router
    } catch (parseError) {
      console.error("Failed to parse Python output:", parseError);
      console.error("Raw Python output:", scriptOutput.output); // Log raw output for debugging
      return NextResponse.json({ error: "Failed to parse Python output", rawOutput: scriptOutput.output }, { status: 500 });
    }
  } catch (error) {
    console.error("API Route error:", error);
    return NextResponse.json({ error: "Internal Server Error" }, { status: 500 });
  }
}