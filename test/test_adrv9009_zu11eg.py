import pytest

hardware = ["adrv9009-dual"]
classname = "adi.adrv9009_zu11eg"


#########################################
@pytest.mark.parametrize("classname, hardware", [(classname, hardware)])
@pytest.mark.parametrize(
    "attr, start, stop, step, tol",
    [
        ("tx_hardwaregain", -89.75, 0.0, 0.25, 0),
        ("trx_lo", 70000000, 6000000000, 1000, 0),
        ("trx_lo_chip_b", 70000000, 6000000000, 1000, 0),
    ],
)
def test_adrv9009_zu11eg_attr(
    test_attribute_single_value, classname, hardware, attr, start, stop, step, tol
):
    test_attribute_single_value(classname, hardware, attr, start, stop, step, tol)


#########################################
@pytest.mark.parametrize("classname, hardware", [(classname, hardware)])
@pytest.mark.parametrize("channel", range(4))
def test_adrv9009_zu11eg_rx_data(test_dma_rx, classname, hardware, channel):
    test_dma_rx(classname, hardware, channel)


#########################################
@pytest.mark.parametrize("classname, hardware", [(classname, hardware)])
@pytest.mark.parametrize("channel", [0])
@pytest.mark.parametrize(
    "param_set",
    [
        dict(
            trx_lo=1000000000,
            gain_control_mode="slow_attack",
            tx_hardwaregain=-10,
            calibrate_rx_qec_en=1,
            calibrate_tx_qec_en=1,
            calibrate=1,
        ),
        dict(
            trx_lo=3000000000,
            gain_control_mode="slow_attack",
            tx_hardwaregain=-10,
            calibrate_rx_qec_en=1,
            calibrate_tx_qec_en=1,
            calibrate=1,
        ),
        dict(
            trx_lo=5000000000,
            gain_control_mode="slow_attack",
            tx_hardwaregain=-10,
            calibrate_rx_qec_en=1,
            calibrate_tx_qec_en=1,
            calibrate=1,
        ),
    ],
)
@pytest.mark.parametrize("sfdr_min", [50])
def test_adrv9009_zu11eg_sfdr(
    test_sfdr, classname, hardware, channel, param_set, sfdr_min
):
    test_sfdr(classname, hardware, channel, param_set, sfdr_min)


#########################################
@pytest.mark.parametrize("classname, hardware", [(classname, hardware)])
@pytest.mark.parametrize("channel", [0])
@pytest.mark.parametrize(
    "param_set",
    [
        dict(
            trx_lo=1000000000,
            gain_control_mode="slow_attack",
            tx_hardwaregain=-20,
            calibrate_tx_qec_en=1,
            calibrate=1,
        ),
        dict(
            trx_lo=3000000000,
            gain_control_mode="slow_attack",
            tx_hardwaregain=-20,
            calibrate_rx_qec_en=1,
            calibrate_tx_qec_en=1,
            calibrate=1,
        ),
        dict(
            trx_lo=5000000000,
            gain_control_mode="slow_attack",
            tx_hardwaregain=-20,
            calibrate_rx_qec_en=1,
            calibrate_tx_qec_en=1,
            calibrate=1,
        ),
    ],
)
@pytest.mark.parametrize("dds_scale, min_rssi, max_rssi", [(0, 35, 60), (0.8, 0, 14)])
def test_adrv9009_zu11eg_dds_gain_check_agc(
    test_gain_check,
    classname,
    hardware,
    channel,
    param_set,
    dds_scale,
    min_rssi,
    max_rssi,
):
    test_gain_check(
        classname, hardware, channel, param_set, dds_scale, min_rssi, max_rssi
    )


#########################################
@pytest.mark.parametrize("classname, hardware", [(classname, hardware)])
@pytest.mark.parametrize("channel", [0])
@pytest.mark.parametrize(
    "param_set, dds_scale, min_rssi, max_rssi",
    [
        (
            dict(
                trx_lo=1000000000,
                gain_control_mode_chan0="manual",
                gain_control_mode_chan1="manual",
                rx_hardwaregain_chan0=0,
                rx_hardwaregain_chan1=0,
                tx_hardwaregain_chan0=-10,
                tx_hardwaregain_chan1=-10,
                calibrate_tx_qec_en=1,
                calibrate=1,
            ),
            0.8,
            30,
            60,
        ),
        (
            dict(
                trx_lo=1000000000,
                gain_control_mode_chan0="manual",
                gain_control_mode_chan1="manual",
                rx_hardwaregain_chan0=30,
                rx_hardwaregain_chan1=30,
                tx_hardwaregain_chan0=-10,
                tx_hardwaregain_chan1=-10,
                calibrate_tx_qec_en=1,
                calibrate=1,
            ),
            0.8,
            0,
            14,
        ),
    ],
)
def test_adrv9009_zu11eg_dds_gain_check_vary_power(
    test_gain_check,
    classname,
    hardware,
    channel,
    param_set,
    dds_scale,
    min_rssi,
    max_rssi,
):
    test_gain_check(
        classname, hardware, channel, param_set, dds_scale, min_rssi, max_rssi
    )


#########################################
@pytest.mark.parametrize("classname, hardware", [(classname, hardware)])
@pytest.mark.parametrize("channel", [0])
@pytest.mark.parametrize(
    "param_set",
    [
        dict(
            trx_lo=1000000000,
            gain_control_mode="slow_attack",
            tx_hardwaregain=-20,
            calibrate_tx_qec_en=1,
            calibrate=1,
        ),
        dict(
            trx_lo=3000000000,
            gain_control_mode="slow_attack",
            tx_hardwaregain=-20,
            calibrate_rx_qec_en=1,
            calibrate_tx_qec_en=1,
            calibrate=1,
        ),
        dict(
            trx_lo=5000000000,
            gain_control_mode="slow_attack",
            tx_hardwaregain=-20,
            calibrate_rx_qec_en=1,
            calibrate_tx_qec_en=1,
            calibrate=1,
        ),
    ],
)
def test_adrv9009_zu11eg_iq_loopback(
    test_iq_loopback, classname, hardware, channel, param_set
):
    test_iq_loopback(classname, hardware, channel, param_set)