import os
import tempfile
import shutil
from file_organizer import organize_by_extension


def test_organize_by_extension():
    """Test that files are correctly organized by extension."""
    tmpdir = tempfile.mkdtemp()

    try:
        open(os.path.join(tmpdir, 'doc1.txt'), 'w').close()
        open(os.path.join(tmpdir, 'doc2.txt'), 'w').close()
        open(os.path.join(tmpdir, 'image.png'), 'w').close()
        open(os.path.join(tmpdir, 'script.py'), 'w').close()
        open(os.path.join(tmpdir, '.hidden'), 'w').close()
        os.makedirs(os.path.join(tmpdir, 'existing_folder'))

        result = organize_by_extension(tmpdir)

        assert result == {'txt': 2, 'png': 1, 'py': 1}
        assert os.path.exists(os.path.join(tmpdir, 'txt', 'doc1.txt'))
        assert os.path.exists(os.path.join(tmpdir, 'png', 'image.png'))
        assert os.path.exists(os.path.join(tmpdir, '.hidden'))

    finally:
        shutil.rmtree(tmpdir)


def test_missing_directory():
    """Test that a missing directory raises FileNotFoundError."""
    try:
        organize_by_extension('/nonexistent/path')
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        pass