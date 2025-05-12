# ✏️ 1. Design Decisions¶
**What were your most important architectural choices?**
The core architectural choice was evolving from simple `str -> str` functions to a streaming `Iterator[str] -> Iterator[str]` model. This shift allowed support for more complex processing like fan-in, fan-out, and stateful logic.

**What abstraction helped you the most?**
Personally, the biggest abstraction win came from treating processors as pluggable units with a consistent interface and making the pipeline fully config-driven using YAML and dynamic imports.

# ⚖️ 2. Tradeoffs¶
To keep development focused, I intentionally skipped full-fledged logging (I added a few bits here and there), lifecycle management, and retry mechanisms. These would be essential in production, especially for debugging failures or issues within the system.

We’re assuming synchronous, linear execution for now. This limits throughput. Async or multiprocess variants could later be swapped in with minimal disruption due to the clean processor abstraction.


# 📈 3. Scalability¶
The line-by-line streaming design ensures memory usage stays constant even as input scales 100x. Since processors are composable and stateless by default, the system is easy to parallelize at the file or partition level.

Maybe, one unique way could be to cache intermediate outputs or results for certain processors. In long chains with expensive operations, this would allow skipping unnecessary computations in reruns.

Also maybe if the system or input grows 100x larger, then, we might need to rethink how to parallelize DAG stages and manage state across workers.

# 🔐 4. Extensibility & Security¶
To run this safely in multi-user environments or production:
- Dynamic imports need strict sandboxing (e.g. via subprocesses or Wasm) to prevent arbitrary code execution.
- Input validation (for config, functions, and whatever inputs are needed from the user)
- Clear separation of trusted and untrusted code (especially for dynamic imports)
- File size limits, and file uploads
- Authentication
- Logging for auditability. Unique pipeline run IDs, and traceable processor execution would help with debugging and compliance.