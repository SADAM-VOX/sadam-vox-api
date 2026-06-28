from core.engine_manager import engine_manager

def run_test():
    print("=== SADAM VOX TEST RUN ===")
    
    result = engine_manager.get("voice_cleaner").process("test_audio.wav")
    
    print("Result:")
    print(result)

if __name__ == "__main__":
    run_test()
