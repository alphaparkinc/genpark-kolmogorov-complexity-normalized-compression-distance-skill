"""Example usage for Normalized Compression Distance Skill."""
from client import NCDCalculator

def main():
    print("Executing NCD Calculator...")
    text_a = "The quick brown fox jumps over the lazy dog."
    text_b = "A quick brown fox jumped over a lazy dog."
    text_c = "9283749817293847192837491827394871293847"

    d_similar = NCDCalculator.distance(text_a, text_b)
    d_dissimilar = NCDCalculator.distance(text_a, text_c)
    print(f"Distance (similar texts): {d_similar}")
    print(f"Distance (dissimilar texts): {d_dissimilar}")

    assert d_similar < d_dissimilar, "Expected similar texts to have smaller NCD"
    
    mat = NCDCalculator.distance_matrix([text_a, text_b, text_c], ["text_a", "text_b", "text_c"])
    print("Distance Matrix:", mat)
    print("NCD Calculator verified successfully!")

if __name__ == "__main__":
    main()
