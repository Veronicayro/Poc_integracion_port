def health():
    return {
        "status": "ok",
        "service": "port-ocean-github-demo",
        "version": "1.0.0",
    }


def main():
    print(health())


if __name__ == "__main__":
    main()
