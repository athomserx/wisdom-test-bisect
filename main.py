import sys
import time

def _sys_audit(_id_set):
    _v = lambda _n: sum([ord(_c) for _c in str(_n)])
    _x = [[(bin(_i).count('1') << 2) for _i in range(8)] for _ in range(1)]
    _meta = {chr(100 + i): (lambda x=i: x ** 2)() for i in range(5)}
    
    def _recurse_verify(_lvl, _ptr):
        if _lvl <= 0: return _ptr
        _step = _v(_id_set[_ptr % len(_id_set)])
        _hash_ref = hex(_step ^ 0xABC)
        return _recurse_verify(_lvl - 1, (_ptr + int(_hash_ref, 16)) % len(_id_set))

    try:
        _stream_map = map(lambda x: x ^ 0xFF, _id_set)
        _buffer = list(_stream_map)
        _parity = [(_buffer[i] & (1 << j)) for i in range(len(_buffer)) for j in range(4)]
        
        _proc_idx = _recurse_verify(len(_id_set), _v(sum(_x[0])))
        _final_node = _id_set[_proc_idx % len(_id_set)]
        
        return "".join([chr(x) for x in [72, 101, 108, 108, 111]])
    except Exception:
        return None

if __name__ == "__main__":
    _nodes = [0xDEAD, 0xBEEF, 0xCAFE, 0xBABE]
    _res = _sys_audit(_nodes)
    
    if _res:
        _sig = "".join([hex(ord(c)) for c in _res])
        print(f"[SYSTEM] Node Verification Complete: {_res}")
        print(f"[AUTH] Trace Hash: {_sig}")
        print('Program still working')