import { useState } from "react";
import "./App.css";

function App() {
  // Image states
  const [imageFile, setImageFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);

  // Mission text
  const [missionText, setMissionText] = useState("");

  // UI state
  const [loading, setLoading] = useState(false);

  // 🔹 Run Detection (NO mock results, backend-ready)
  const handleRunDetection = () => {
    setLoading(true);

    // Placeholder for backend API call
    setTimeout(() => {
      setLoading(false);
    }, 1200);
  };

  return (
    <div className="app">
      <header className="header">
        Identify the Imposter Pokémon
        <span className="status">
          {loading ? "Processing..." : "Ready"}
        </span>
      </header>

      <div className="layout">
        {/* LEFT COLUMN */}
        <div className="left">
          <div className="card">
            <h3>Upload Image</h3>
            <p className="subtitle">Select an image to detect objects</p>

            {/* IMAGE UPLOAD */}
            <div className="upload-box">
              <input
                type="file"
                accept="image/png, image/jpeg, image/webp"
                onChange={(e) => {
                  const file = e.target.files[0];
                  if (!file) return;

                  setImageFile(file);
                  setImagePreview(URL.createObjectURL(file));
                }}
              />

              <p>
                Drop your image here <br />
                or click to browse
              </p>

              <span>Supports PNG, JPG, WEBP</span>
            </div>

            {/* MISSION TEXT */}
            <div className="mission-box" style={{ marginTop: "16px" }}>
              <h3>Mission Instructions</h3>
              <p className="subtitle">
                Describe which Pokémon to attack and protect
              </p>

              <textarea
                value={missionText}
                onChange={(e) => setMissionText(e.target.value)}
                placeholder={`Enter mission instructions here...
Example:
Neutralize all Bulbasaurs.
Do not harm Pikachu or Charizard.`}
              />

              <span className="mission-help">
                This text is used to identify target and protected Pokémon.
              </span>
            </div>

            {/* RUN DETECTION */}
            <button
              className="run-btn"
              onClick={handleRunDetection}
              disabled={!imageFile || !missionText || loading}
            >
              {loading ? "Running Detection..." : "Run Detection"}
            </button>
          </div>

          {/* RESULTS */}
          <div className="card">
            <h3>Results</h3>
            <div className="empty">
              <p>No detections yet</p>
              <span>Upload an image and run detection</span>
            </div>
          </div>
        </div>

        {/* RIGHT COLUMN */}
        <div className="card preview">
          <h3>Detection Preview</h3>

          <div className="preview-box">
            {imagePreview ? (
              <img
                src={imagePreview}
                alt="Preview"
                style={{
                  maxWidth: "100%",
                  maxHeight: "100%",
                  borderRadius: "12px",
                  objectFit: "contain",
                }}
              />
            ) : (
              <>
                <p>No image selected</p>
                <span>Upload an image to start detection</span>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
