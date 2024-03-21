from cringelord.service.models.cringe_mode import CringeMode


class TestCringeMode:
    class TestCreation:
        def test(self):
            _ = CringeMode("ALL")
            _ = CringeMode.ALL
            _ = CringeMode("SRC")
            _ = CringeMode.SRC

    class TestEquality:
        def test(self):
            assert CringeMode.ALL == "ALL"
            assert CringeMode.SRC == "SRC"

        def test_membership(self):
            assert "ALL" in CringeMode
            assert CringeMode.ALL in CringeMode
            assert "SRC" in CringeMode
            assert CringeMode.SRC in CringeMode
