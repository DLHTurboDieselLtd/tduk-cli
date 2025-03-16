import argparse

def configure_git():
    return (
        "Configuring Git...\n"
        "Username: <username>\n"
        "Email: <email>\n"
        "Default Branch: main\n"
        "Commit Template: <template>"
    )

def checklist_dry_run():
    actual_output = (
        "Dry run mode enabled. No changes will be made.\n"
        "Checklist:\n"
        "- Task 1\n"
        "- Task 2\n"
        "- Task 3"
    )
    return actual_output

def onboard_command(args):
    if args.all:
        print(configure_git())
    elif args.task:
        if args.task == "git":
            print(configure_git())
        elif args.task == "checklist" and args.dry_run:
            print(checklist_dry_run())
        else:
            print(f"Unknown task: {args.task}")
    elif args.configure:
        if args.configure == "git":
            print(configure_git())
        else:
            print(f"Unknown dev tool: {args.configure}")
    else:
        print("No valid arguments provided for onboard command.")


def main():
    parser = argparse.ArgumentParser(prog="tduk-cli")
    subparsers = parser.add_subparsers(dest="command")

    # Add onboard subcommand
    onboard_parser = subparsers.add_parser("onboard", help="Run onboarding tasks")
    onboard_parser.add_argument("--all", action="store_true", help="Run all onboarding tasks")
    onboard_parser.add_argument("--task", type=str, help="Run a specific onboarding task")
    onboard_parser.add_argument("--configure", type=str, help="Configure a specific dev tool")
    onboard_parser.add_argument("--dry-run", action="store_true", help="Run in dry-run mode")

    # Parse arguments and call appropriate function
    args = parser.parse_args()
    if args.command == "onboard":
        onboard_command(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
