import { useState } from "react";
import { motion } from "framer-motion";
import { ShieldAlert } from "lucide-react";

export default function App() {
  const [form, setForm] = useState({
    total_changes: 0,
    total_lines_added: 0,
    total_lines_deleted: 0,
    avg_complexity: 0,
    avg_loc: 0,
    num_authors: 0,
    bug_fix_commits: 0,
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: Number(e.target.value) });
  };

  const predict = async () => {
  setLoading(true);

  try {
    const res = await fetch("https://bug-prediction-system-backend.onrender.com", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    });

    const data = await res.json();
    setResult(data);

  } catch (error) {
    console.error(error);
    alert("Request failed: " + error.message);
  } finally {
    setLoading(false);
  }
};

  const fields = Object.keys(form);

  return (
    <div className="min-h-screen p-8 relative overflow-hidden">
      {/* Background Effects */}
      <div className="absolute w-72 h-72 bg-cyan-500/20 blur-3xl rounded-full top-10 left-10 animate-pulse"></div>
      <div className="absolute w-80 h-80 bg-fuchsia-500/20 blur-3xl rounded-full bottom-10 right-10 animate-pulse"></div>

      <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-8 relative z-10">
        {/* Left Card */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white/10 backdrop-blur-xl border border-white/10 rounded-3xl p-8 shadow-2xl"
        >
          <h1 className="text-4xl font-bold mb-2">Bug Prediction System</h1>
          <p className="text-slate-300 mb-6">
            AI-powered repository defect risk analysis
          </p>

          <div className="grid grid-cols-2 gap-4">
            {fields.map((field) => (
              <input
                key={field}
                name={field}
                type="number"
                placeholder={field.replaceAll("_", " ")}
                onChange={handleChange}
                className="p-3 rounded-xl bg-white/5 border border-white/10 outline-none focus:border-cyan-400"
              />
            ))}
          </div>

          <button
            onClick={predict}
            className="mt-6 w-full py-3 rounded-xl bg-cyan-400 text-slate-900 font-bold hover:scale-105 transition duration-300"
          >
            {loading ? "Analyzing..." : "Analyze Risk"}
          </button>
        </motion.div>

        {/* Right Card */}
        <motion.div
          initial={{ opacity: 0, scale: 0.85 }}
          animate={{ opacity: 1, scale: 1 }}
          className="bg-white/10 backdrop-blur-xl border border-white/10 rounded-3xl p-8 shadow-2xl flex flex-col justify-center items-center"
        >
          <ShieldAlert size={72} className="text-cyan-300 mb-4" />

          {result ? (
            <>
              <h2 className="text-6xl font-bold">
                {Math.round(result.bug_probability * 100)}%
              </h2>

              <p className="text-2xl mt-3 font-semibold">
                {result.risk_level} RISK
              </p>

              <div className="w-full bg-white/10 rounded-full h-5 mt-8 overflow-hidden">
                <div
                  className="bg-cyan-400 h-5 transition-all duration-700"
                  style={{
                    width: `${Math.round(result.bug_probability * 100)}%`,
                  }}
                ></div>
              </div>

              <p className="text-slate-300 mt-4">
                Probability: {result.bug_probability}
              </p>
            </>
          ) : (
            <p className="text-slate-300 text-center text-lg">
              Enter metrics and click Analyze Risk.
            </p>
          )}
        </motion.div>
      </div>
    </div>
  );
}
