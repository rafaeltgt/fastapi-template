import typer
from rich.console import Console
from rich.table import Table
from sqlmodel import Session, select

from fastapi_template.database import engine
from fastapi_template.models.user import SQLModel, User
from fastapi_template.security import get_password_hash
from fastapi_template.settings import Settings

main = typer.Typer(name='APP CLI')


@main.command()
def shell():
    """Opens interactive shell"""
    _vars = {
        'settings': Settings(),
        'engine': engine,
        'select': select,
        'session': Session(engine),
        'User': User,
    }
    typer.echo(f'Auto imports: {list(_vars.keys())}')
    try:
        from IPython import start_ipython  # noqa: PLC0415

        start_ipython(
            argv=['--ipython-dir=/tmp', '--no-banner'], user_ns=_vars
        )
    except ImportError:
        import code  # noqa: PLC0415

        code.InteractiveConsole(_vars).interact()


@main.command()
def user_list():
    """Lists all users"""
    table = Table(title='Pamps users')
    fields = ['username', 'email']
    for header in fields:
        table.add_column(header, style='magenta')

    with Session(engine) as session:
        users = session.exec(select(User))
        for user in users:
            table.add_row(user.username, user.email)

    Console().print(table)


@main.command()
def create_user(email: str, username: str, password: str):
    """Create user"""

    hashed_password = get_password_hash(password)

    with Session(engine) as session:
        user = User(email=email, username=username, password=hashed_password)
        session.add(user)
        session.commit()
        session.refresh(user)
        typer.echo(f'created {username} user')
        return user


@main.command()
def reset_db(
    force: bool = typer.Option(
        False, '--force', '-f', help='Run with no confirmation'
    ),
):
    """Resets the database tables"""
    force = force or typer.confirm('Are you sure?')
    if force:
        SQLModel.metadata.drop_all(engine)


if __name__ == '__main__':
    main()
