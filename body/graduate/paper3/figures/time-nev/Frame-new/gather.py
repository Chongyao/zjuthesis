import os
import re
import csv
import glob


def remove_ansi_codes(text):
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", text)


def parse_cms(content):
    """Parse CB-CMS logs: CMS::solve time and Acc Err Num"""
    content = remove_ansi_codes(content)
    time_val = None
    conv_val = None

    # [TOC] CMS::solve time: 24.652 s
    time_match = re.search(r"CMS::solve time:\s+([\d\.]+)\s+s", content)
    if time_match:
        time_val = time_match.group(1)

    # Acc Err Num: 18
    conv_match = re.search(r"Acc Err Num:\s+(\d+)", content)
    if conv_match:
        conv_val = conv_match.group(1)

    return conv_val, time_val


def parse_cms_intrd(content):
    """Parse CMS-INTRD logs: sum of CMS::solve, set interface modes, construct K/M, solve reduced"""
    content = remove_ansi_codes(content)

    # 1. CMS::solve time (may have multiple, sum them)
    cms_solve_times = re.findall(r"CMS::solve time:\s+([\d\.]+)\s+s", content)
    if not cms_solve_times:
        return None, "计算结果有问题"
    sum_cms_solve = sum(float(t) for t in cms_solve_times)

    # 2. set interface modes cost
    set_interface_match = re.search(
        r"TOC: set interface modes cost\s+([\d\.]+)\s+seconds", content
    )
    set_interface_time = (
        float(set_interface_match.group(1)) if set_interface_match else 0.0
    )

    # 3. construct reduced K, M cost
    construct_km_match = re.search(
        r"TOC: construct reduced K, M cost\s+([\d\.]+)\s+seconds", content
    )
    construct_km_time = (
        float(construct_km_match.group(1)) if construct_km_match else 0.0
    )

    # 4. solve reduced eigen cost
    solve_reduced_match = re.search(
        r"TOC: solve reduced eigen cost\s+([\d\.]+)\s+seconds", content
    )
    solve_reduced_time = (
        float(solve_reduced_match.group(1)) if solve_reduced_match else 0.0
    )

    total_time = (
        sum_cms_solve + set_interface_time + construct_km_time + solve_reduced_time
    )

    # Conv: Total num below threshold
    conv_match = re.search(r"Total num below threshold:\s+(\d+)", content)
    conv_val = conv_match.group(1) if conv_match else None

    return conv_val, f"{total_time:.6f}"


def parse_pd(content):
    """Parse PD logs: sum of [TOC] solve time, set interface modes, construct K/M, solve reduced"""
    content = remove_ansi_codes(content)

    # 1. Sum of [TOC] solve time (there are two: primal and dual partitions)
    solve_times = re.findall(r"\[TOC\] solve time:\s+([\d\.]+)\s+s", content)
    sum_solve_time = sum(float(t) for t in solve_times)

    # 2. set interface modes cost
    set_interface_match = re.search(
        r"TOC: set interface modes cost\s+([\d\.]+)\s+seconds", content
    )
    set_interface_time = (
        float(set_interface_match.group(1)) if set_interface_match else 0.0
    )

    # 3. construct reduced K, M cost
    construct_km_match = re.search(
        r"TOC: construct reduced K, M cost\s+([\d\.]+)\s+seconds", content
    )
    construct_km_time = (
        float(construct_km_match.group(1)) if construct_km_match else 0.0
    )

    # 4. solve reduced eigen cost (NOT divided by 7 anymore in new format)
    solve_reduced_match = re.search(
        r"TOC: solve reduced eigen cost\s+([\d\.]+)\s+seconds", content
    )
    solve_reduced_time = (
        float(solve_reduced_match.group(1)) if solve_reduced_match else 0.0
    )

    total_time = (
        sum_solve_time + set_interface_time + construct_km_time + solve_reduced_time
    )

    # Conv: Total num below threshold
    conv_match = re.search(r"Total num below threshold:\s+(\d+)", content)
    conv_val = conv_match.group(1) if conv_match else None

    return conv_val, f"{total_time:.6f}"


def parse_amls(content):
    """Parse AMLS logs: AMLS Elapsed time and Number of valid eigenvalues"""
    content = remove_ansi_codes(content)

    # 1. AMLS Elapsed time: 8.665957(s)
    time_match = re.search(r"AMLS Elapsed time:\s+([\d\.]+)\(s\)", content)
    time_val = time_match.group(1) if time_match else None

    # 2. Conv - Number of valid eigenvalues (cumulative 2-norm error < X.XXXXXXe-XX): N
    conv_match = re.search(
        r"Number of valid eigenvalues \(cumulative 2-norm error < [\d\.e\-\+]+\):\s+(\d+)",
        content,
    )
    conv_val = conv_match.group(1) if conv_match else None

    return conv_val, time_val


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    results = []

    # Get all subdirectories starting with NEP_
    dirs = [
        d
        for d in os.listdir(root_dir)
        if os.path.isdir(os.path.join(root_dir, d)) and d.startswith("NEP_")
    ]

    for d in sorted(dirs):
        parts = d.split("_")
        # Structure: NEP_xx_yy or NEP_xx_yy_zz
        # xx is parts[1] (NEP value)
        # yy... is parts[2:] joined by _ (algorithm)

        if len(parts) < 3:
            continue

        nep_val = parts[1]
        algorithm_suffix = "_".join(parts[2:])

        # Determine log file name based on algorithm
        if algorithm_suffix == "CMSINTRD_4_5":
            log_pattern = "result.log"
        else:
            log_pattern = "run.log"

        log_files = glob.glob(os.path.join(root_dir, d, log_pattern))
        if not log_files:
            # Try any .log file as fallback
            log_files = glob.glob(os.path.join(root_dir, d, "*.log"))

        if not log_files:
            print(f"Warning: No log files found in {d}")
            continue

        for log_file in log_files:
            with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            conv = None
            time_val = None
            algorithm_name = None

            # Map algorithm suffix to parser and standard name
            if algorithm_suffix == "CB-CMS":
                conv, time_val = parse_cms(content)
                algorithm_name = "CMS"  # Keep as CMS for compatibility with plot.py
            elif algorithm_suffix == "CMSINTRD_4_5":
                conv, time_val = parse_cms_intrd(content)
                algorithm_name = "CMSINTRD"
            elif algorithm_suffix == "AMLS":
                conv, time_val = parse_amls(content)
                algorithm_name = "AMLS"
            elif algorithm_suffix == "PD":
                conv, time_val = parse_pd(content)
                algorithm_name = "PD"
            else:
                print(f"Warning: Unknown algorithm suffix: {algorithm_suffix} in {d}")
                continue

            if time_val is not None and time_val != "计算结果有问题":
                results.append(
                    {
                        "algorithm": algorithm_name,
                        "nev": conv if conv else "N/A",
                        "time": time_val,
                    }
                )
                print(
                    f"Parsed {d}: algorithm={algorithm_name}, nev={conv}, time={time_val}"
                )
            else:
                print(f"Warning: Failed to parse {d}: time={time_val}")

    # Sort by algorithm and nev
    def sort_key(r):
        try:
            nev = int(r["nev"]) if r["nev"] != "N/A" else 0
        except:
            nev = 0
        return (r["algorithm"], nev)

    results.sort(key=sort_key)

    # Write CSV (format: algorithm, nev, time)
    output_file = os.path.join(os.path.dirname(root_dir), "nev-time-new.csv")
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["algorithm", "nev", "time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"\nOutput written to: {output_file}")
    print(f"Total records: {len(results)}")


if __name__ == "__main__":
    main()
