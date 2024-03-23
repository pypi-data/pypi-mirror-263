#!/usr/bin/env python3
import argparse
import glob
import os
from pathlib import Path


def main():

    parser = argparse.ArgumentParser(description="Clean up powheg directory")

    # Adding optional argument with default value
    parser.add_argument(
        "-p", "--path", default=".", type=str, help="path to powheg directory"
    )

    args = parser.parse_args()

    # remove single file
    for f in [
        "bornequiv",
        "pwg-btlgrid.top",
        "pwggrid.dat",
        "pwgubound.dat",
        "realequivregions-btl",
        "FlavRegList",
        "pwgborngrid.top",
        "pwgcounters.dat",
        "pwghistnorms.top",
        "pwgxgrid.dat",
        "realequivregions-rad",
        "pwgboundviolations.dat",
        "pwgevents.lhe",
        "pwg-stat.dat",
        "pwhg_checklimits",
        "virtequiv",
        "parameters.ol",
        "mint_upb_rmupb.top",
        "mint_upb_btlupb.top",
        "mint_upb_btlupb_rat.top",
        "pwg-btilde-fullgrid.lock",
        "pwg-remn-fullgrid.lock",
    ]:
        p = os.path.join(args.path, f)
        if os.path.exists(p):
            os.remove(p)
    # remove parallel run files
    for n, s in [
        ("pwggrid-rm-", ".dat"),
        ("pwggrid-btl-", ".dat"),
        ("pwgrmupb-", ".dat"),
        ("pwgbtlupb-", ".dat"),
        ("pwgboundviolations-", ".dat"),
        ("pwghistnorms-", ".top"),
        ("pwgevents-", ".lhe"),
        ("pwgcounters-st4-", ".dat"),
        ("pwgcounters-st3-", ".dat"),
        ("pwgcounters-st1-", ".dat"),
        ("pwgcounters-st2-", ".dat"),
        ("pwg-xg1-btl-", ".top"),
        ("pwg-xg1-xgrid-btl-", ".dat"),
        ("pwg-xg1-xgrid-rm-", ".dat"),
        ("pwg-xg2-xgrid-btl-", ".dat"),
        ("pwg-xg2-xgrid-rm-", ".dat"),
        ("pwg-xg2-xgrid-btl-", ".top"),
        ("pwg-xg2-xgrid-rm-", ".top"),
        ("pwg-st2-xgrid-btl-", ".top"),
        ("pwg-st2-xgrid-rm-", ".top"),
        ("pwgubound-", ".dat"),
        ("sigborn_equiv-", ""),
        ("sigvirtual_equiv-", ""),
        ("sigreal_btl0_equiv-", ""),
        ("sigreal_rad_equiv-", ""),
        ("pwgalone-output", ".top"),
        ("pwgfullgrid-btl-", ".dat"),
        ("pwgfullgrid-rm-", ".dat"),
        ("pwhg_checklimits-", ""),
        ("pwg-", "-NLO.top"),
        ("pwg-", "-borngrid-stat.dat"),
        ("pwg-", "-xg1-stat.dat"),
        ("pwg-", "-xg2-stat.dat"),
        ("pwg-", "-st3-stat.dat"),
        ("pwg-", "-st2-stat.dat"),
    ]:
        for f in Path(args.path).glob(f"{n}*{s}"):
            os.remove(f)


if __name__ == "__main__":
    main()
