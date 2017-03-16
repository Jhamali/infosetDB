#!/usr/bin/env python3
"""infoset CLI functions for 'restart'.

Functions to restart daemons

"""

# Main python libraries
import sys

# Infoset-NG imports
from infoset.utils import general
from infoset.main.agent import Agent, AgentAPI, AgentDaemon
from infoset.constants import (
    API_EXECUTABLE, API_GUNICORN_AGENT, POLLER_EXECUTABLE)


def run(args):
    """Process 'restart' command.

    Args:
        args: Argparse arguments

    Returns:
        None

    """
    # Show help if no arguments provided
    if args.qualifier is None:
        general.cli_help()

    # Process 'show api' command
    if args.qualifier == 'api':
        api(args)
    elif args.qualifier == 'poller':
        poller(args)

    # Show help if there are no matches
    general.cli_help()
    sys.exit(2)


def api(args):
    """Process 'restart api' commands.

    Args:
        args: Argparse arguments

    Returns:
        None

    """
    # Create agent objects
    agent_gunicorn = Agent(API_GUNICORN_AGENT)
    agent_api = AgentAPI(API_EXECUTABLE, API_GUNICORN_AGENT)

    # Restart daemons
    daemon_gunicorn = AgentDaemon(agent_gunicorn)
    daemon_api = AgentDaemon(agent_api)
    if args.force is True:
        daemon_gunicorn.force()
        daemon_api.force()
    daemon_gunicorn.restart()
    daemon_api.restart()

    # Done
    sys.exit(0)


def poller(args):
    """Process 'restart poller' commands.

    Args:
        args: Argparse arguments

    Returns:
        None

    """
    # Create agent object
    agent_poller = Agent(POLLER_EXECUTABLE)

    # Restart daemon
    daemon_poller = AgentDaemon(agent_poller)
    if args.force is True:
        daemon_poller.force()
    daemon_poller.restart()

    # Done
    sys.exit(0)
