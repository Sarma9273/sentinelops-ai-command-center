from pathlib import Path


def test_core_files_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "backend" / "incident_case_generator.py").exists()
    assert (root / "ml_engine" / "risk_scoring_engine.py").exists()
    assert (root / "index.html").exists()
